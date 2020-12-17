import sys
import os
import psutil

from lib.tools.utils import success, info, warning, error


class Porccesser(object):
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.targets = None
        self.port = 80

    def pskill(self, pid):
        proccess = psutil.Proccess(pid)
        for proc in proccess.children(recursive=True):
            proc.kill()
        proccess.kill()

    def start(self):
        try:
            while True:
                try:
                    self.command = input("Linx > ")
                except EOFError:
                    self.command = "exit"

                self.input_list = self.command.split()

                try:
                    if self.command == "help":
                        print("help")
                    elif self.command == "exit" or self.command == "quit":
                        exit()
                    elif self.input_list[0] == "crawler" or self.input_list[0] == "CRAWLER":
                        try:
                            pass
                        except IndexError:
                            pass
                    elif self.input_list[0] == "scan" or self.input_list[0] == "SCAN":
                        try:
                            pass
                        except IndexError:
                            pass
                except IndexError:
                    pass
                except Exception as e:
                    pass
                except KeyboardInterrupt:
                    exit(0)
        except KeyboardInterrupt:
            exit(0)
