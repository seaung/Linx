import os
import sys
import time
import psutil

from lib.tools.utils import success, info, warning, error, colors
from lib.tools.helper import show_help, show_crawler_help, show_scanner_help
from modules.isopsys import show_opt_sys
from modules.scan import run_default_scan

class Processer(object):
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.port = 80
        self.input_list = None

    def pskill(self, pid):
        process = psutil.Process(pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()

    def start(self):
        try:
            while True:
                try:
                    self.command = input("Lins > ")
                except EOFError:
                    self.command = "exit"

                self.input_list = self.command.split()

                try:
                    if self.command == "help" or self.command == "show":
                        show_help()
                    elif self.command == "exit" or self.command == "quit":
                        print(info("[*] User requested shutdown..."))
                        exit(0)
                    elif self.input_list[0] == "crawler" or self.input_list[0] == "CRAWLER":
                        try:
                            if self.input_list[1] == "show":
                                show_crawler_help()
                            else:
                                self.url = self.input_list[1]
                                print("crawler in... ", self.url)
                        except IndexError:
                            print("[*] Enter a url please !")
                    elif self.input_list[0] == "scanner" or self.input_list[0] == "SCANNER":
                        try:
                            if self.input_list[1] == "show":
                                show_scanner_help()
                            else:
                                self.target = self.input_list[1]
                                print("scanner in ... ", self.target)
                                start_time = time.time()
                                run_default_scan(self.target)
                                print(success(f"scan used time is : {time.time()-start_time}'s"))
                        except IndexError:
                            print("[*] Enter a target ip addresses !")
                    elif self.input_list[0] == "system" or self.input_list[0] == "SYS":
                        try:
                            if self.input_list[1] == "show":
                                print("show system.")
                            else:
                                self.host = self.input_list[1]
                                show_opt_sys(self.host)
                        except IndexError:
                            print("[*] system press key.")
                except IndexError:
                    pass

        except KeyboardInterrupt:
            exit(0)
