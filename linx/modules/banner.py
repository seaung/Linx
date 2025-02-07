from random import randint
from modules.helper import color


def print_banner() -> str:
    banner = '''
    ██╗     ██╗███╗   ██╗██╗  ██╗
    ██║     ██║████╗  ██║╚██╗██╔╝
    ██║     ██║██╔██╗ ██║ ╚███╔╝ 
    ██║     ██║██║╚██╗██║ ██╔██╗ 
    ███████╗██║██║ ╚████║██╔╝ ██╗
    ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
    '''
    baNNer = '''
     _      _____  _   _ __   __
    | |    |_   _|| \ | |\ \ / /
    | |      | |  |  \| | \ V / 
    | |      | |  | . ` |  > <  
    | |____ _| |_ | |\  | / . \ 
    |______|_____||_| \_|/_/ \_\
    
    '''
    attrs = [banner, baNNer]
    return attrs[randint(0, 1)]