import sys
import os

from lib.core.processer import Processer
from config.ascii import show_banner


version = "0.1.0"
#author = "seaung"
author = "70ty"

p = Processer()


if __name__ == "__main__":
    if os.geteuid() != 0:
        sys.exit("[!] Only for roots kido!")
    try:
        print(show_banner())
        print()
        p.start()
    except Exception as e:
        #print("[!] Exception Unkonow Error : {}".format(e))
        print("[!] Exception caught : {}".format(e))
