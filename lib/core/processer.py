import sys
import os
import psutil

from lib.tools.utils import success, info, warning, error
from lib.tools.helper import show_help, show_crawler_help, show_scanner_help


class Processer(object):
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.port = 80
        self.input_list = None

    def pskill(self, pid):
        proccess = psutil.Proccess(pid)
        for proc in proccess.children(recursive=True):
            proc.kill()
        proccess.kill()

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
                        print("[*] User requested shutdown...")
                        exit()
                    elif self.input_list[0] == "crawler" or self.input_list[0] == "CRAWLER":
                        #print(self.input_list)
                        try:
                            if self.input_list[1] == "show":
                                show_crawler_help()
                            else:
                                self.url = self.input_list[1]
                                print("crawler in...", self.url)
                        except IndexError:
                            print("[*] Enter a url please !")
                            pass
                    elif self.input_list[0] == "scanner" or self.input_list[0] == "SCANNER":
                        try:
                            pass
                        except IndexError:
                            print("[*] Enter a target ip addresses !")
                            pass

                except IndexError:
                    pass

        except KeyboardInterrupt:
            exit(0)
