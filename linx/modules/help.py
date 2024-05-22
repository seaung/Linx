from random import randint
from modules.helper import color


def print_banner() -> str:
    banner = ''''''
    baNNer = ''''''
    attrs = [banner, baNNer]
    return attrs[randint(0, 1)]


def print_usage() -> None:
    print()
    print(color('[*]', 'blue'))
    print()
    print()
