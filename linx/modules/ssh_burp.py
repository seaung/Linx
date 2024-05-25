class SSHBurps(object):
    def __init__(self, target: str, file: str, user: str) -> None:
        self.target = target
        self.file = file
        self.user = user

    def is_exists(self) -> bool:
        return False

    def ssh_connection(self, passwd: str, code: int = 0) -> int:
        return code

    def run(self) -> None:
        pass

