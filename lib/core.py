import sys
import os
import psutil
import termcolor

from commons.utils import save_command
from commons.utils import print_usage

from lib.completer import Completer


class Porccesser(object):
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))

        self.targets = None
        self.file = None
        self.port = 80
        self.domain = None

    def pskill(self, proccess_id):
        proccess = psutil.Proccess(proccess_id)
        for proc in proccess.children(recursive=True):
            proc.kill()
        proccess.kill()

    def start(self):
        try:
            save_command("")
            while True:
                completer = Completer(self.path, "linx")
                console = termcolor.colored("Linx>", "red", attrs=["bold"])
                try:
                    self.command = input("{} ".format(console))
                except EOFError:
                    self.command = "exit"

                save_command(self.command)
                self.input_list = self.command.split()

                try:
                    if self.command == "help":
                        print_usage()
                    elif self.command == "exit" or self.command == "quit":
                        print("[*] User Requested Shutdown.")
                        exit()
                    elif self.input_list[0] == "set" or self.input_list[0] == "SET":
                        try:
                            if self.input_list[1] == "port":
                                try:
                                    self.port = int(self.input_list[2])
                                except IndexError:
                                    try:
                                        self.port = input("[+] Enter the default port : ")
                                    except KeyboardInterrupt:
                                        pass
                            elif self.input_list[1] == "domain":
                                try:
                                    self.domain = self.input_list[2]
                                except IndexError:
                                    try:
                                        self.domain = input("[+] Enter the target domain : ")
                                    except KeyboardInterrupt:
                                        pass
                            elif self.input_list[1] == "target":
                                try:
                                    self.targets = self.input_list[2]
                                except IndexError:
                                    try:
                                        self.targets = input("[+] Enter the target(s) : ")
                                    except KeyboardInterrupt:
                                        pass
                            elif self.input_list[1] == "file":
                                try:
                                    self.file = self.input_list[2]
                                except IndexError:
                                    try:
                                        self.file = input("[+] Enter the file path : ")
                                    except KeyboardInterrupt:
                                        pass
                            elif self.input_list[1] == "help":
                                print("\n[Hlep] Select a variable to set")
                                print("Exmple:")
                                print("{} set port\n".format(console))

                        except IndexError:
                            print("[!] Select a valid variable to set.")

                    elif self.input_list[0] == "print":
                        try:
                            if self.input_list[1] == "port":
                                print("[+] Default port {}".format(self.port))
                            elif self.input_list[1] == "domain":
                                print("[+] The target domain {}".format(self.domain))
                            elif self.input_list[1] == "file":
                                print("[+] Payload file {}".format(self.file))
                            elif self.input_list[1] == "target":
                                print("[+] Set target {}".format(self.targets))
                            else:
                                print("\n[Hlep]")
                                print("Exmple:")
                                print("")
                        except IndexError:
                            print("[!] Please select a variable name")
                    elif self.input_list[0] == "crawler":
                        if self.input_list[1] == "help":
                            print("\n[Help] run a web crawler in target URL.")
                            print("[Required] URL as target")
                            print("example:")
                            print("{} set target http://www.example.com/id=1".format(console))
                            print("{} webcrawler start\n".format(console))
                        elif self.input_list[1] == "run":
                            from linx.modules.webcrawler import WebCrawler
                            self.webcrawler = WebCrawler()
                            try:
                                self.webcrawler.crawler(self.input_list[2])
                            except IndexError:
                                try:
                                    if self.targets:
                                        self.webcrawler.crawler(self.targets)
                                    else:
                                        self.targets = input("[+] Enter the target URL:")
                                        self.webcrawler.crawler(self.targets)
                                except KeyboardInterrupt:
                                    pass
                                except Exception as e:
                                    print("[!] crawler exception: {}".format(e))
                                    print("[!] Exception caught: {}".format(e))
                                except Exception as e:
                                    print("[!] Exception form crawler: {}".format(e))
                                    print("[!] Exception caught: {}".format(e))
                except IndexError:
                    pass
                except Exception as e:
                    print()
                except KeyboardInterrupt:
                    print("\n[*] User Requested Shutdown.")
                    exit()
        except Exception as e:
            print("\n[*] User Requested Shutdown.")
            eixt()
