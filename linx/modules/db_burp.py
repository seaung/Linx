class DBBurp(object):
    def __init__(self, target: str, file: str, port: int = 3306) -> None:
        self.target = target
        self.port = port
        self.file = file

    def is_exists(self) -> bool:
        return False

    def connection(self, target: str, port: int, passwd: str) -> bool:
        return False

    def run(self) -> bool:
        return False
