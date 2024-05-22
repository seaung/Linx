import sys
import os


version = "1.0.0"

author = "seaung"


if __name__ == "__main__":
    if os.geteuid() != 0:
        sys.exit("[!] Only for roots kido!")
    try:
        pass
    except Exception as e:
        print("[!] Exception caught : {}".format(e))

