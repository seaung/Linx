import os
import sys
import termcolor

from lib.tools.helper import show_help, show_crawler_help, show_scanner_help
from lib.tools.utils import colors


class Processer(object):
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.port = 80
        self.input_list = None

    def start(self):
        try:
            while True:
                console = termcolor.colored("Lins > ", "red", attrs=["bold"])
                try:
                    self.command = input(f"{console}")
                except EOFError:
                    self.command = "exit"

                self.input_list = self.command.split()

                try:
                    if self.command == "help" or self.command == "show":
                        show_help()
                    elif self.command == "exit" or self.command == "quit":
                        print(colors("[*] User requested shutdown...", "green"))
                        exit()
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
                        except IndexError:
                            print("[*] Enter a target ip addresses !")
                    elif self.input_list[0] == "system" or self.input_list[0] == "SYS":
                        try:
                            if self.input_list[1] == "show":
                                print("show system.")
                            else:
                                self.host = self.input_list[1]
                        except IndexError:
                            print("[*] system press key.")
                except IndexError:
                    pass

        except KeyboardInterrupt:
            exit()
