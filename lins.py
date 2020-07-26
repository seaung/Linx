import sys
import os

from lib.core import Porccesser
from commons.utils import print_logo, colors


version = "0.1.0"
#author = "seaung"
author = "70ty"

p = Porccesser()


if __name__ == "__main__":
    if os.geteuid() != 0:
        sys.exit("[!] Only for roots kido!")

    try:
        print(print_logo(version, author))
        print()
        p.start()
    except Exception as e:
        #print("[!] Exception Unkonow Error : {}".format(e))
        print("[!] Exception caught : {}".format(e))

