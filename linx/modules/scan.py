class Scanner(object):
    def __init__(self, target: str, port: list = []) -> None:
        if port is None:
            self.ports = [21, 22, 23, 25, 53, 57, 79, 80, 107]
        else:
            self.ports = port

        self.target = target

    def port_scan(self) -> None:
        pass

    def tcp_scan(self) -> None:
        pass

