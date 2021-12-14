from termcolor import colored


def show_help():
    print(colored("Lins > crawler show | help", "green"))
    print(colored("Lins > crawler target url(e.g https://www.baidu.com)", "green"))
    print(colored("lins > crawler https://www.baidu.com", "green"))

    print(colored("====================================================", "green"))

    print(colored("Lins > scanner show | help", "green"))
    print(colored("Lins > scanner target ip addresses (e.g 192.168.7.1)", "green"))
    print(colored("Lins > scanner 192.168.7.1", "green"))


def show_crawler_help():
    print(colored("Lins > crawler show | help (show help info.)", "green"))
    print(colored("Lins > crawler show | help", "green"))
    print(colored("Lins > crawler target url (e.g https://www.baidu.com)", "green"))
    print(colored("Lins > crawler https://www.baidu.com", "green"))


def show_scanner_help():
    print(colored("Lins > scanner show | help (show help info.)", "green"))
    print(colored("Lins > scanner show | help", "green"))
    print(colored("Lins > scanner target url (e.g 192.168.7.1)", "green"))
    print(colored("LIns > scanner 192.168.7.1", "green"))

