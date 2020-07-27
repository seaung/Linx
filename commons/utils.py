import termcolor
import hashlib


def get_md5(value):
    if isinstance(value, str):
        value = value.encode(encoding="utf-8")
    return hashlib.md5(value).hexdigest()


def save_command(cmd):
    try:
        with open('.linx_history', 'a+') as fs:
            fs.write('{}\n'.format(cmd))
    except Exception as e:
        print("[!] save command caught: {}".format(e))
        print("[!] Exception caught : {}".format(e))
        pass


def colors(message, color):
    msg = termcolor.colored(str(meesage), str(color), attrs=["bold"])
    return msg


def print_logo(version, author):
    banner = '''\n
             _     _            
            | |   (_)_ __ __  __
            | |   | | '_    \/ /
            | |___| | | | |>  < 
            |_____|_|_| |_/_/\_

        [ Linx - Penetration Testing Tools ]
        [ Author by {0} ]
        [ version {1} ]
    '''.format(author, version)
    return colors(banner, "green")


def print_usage():
    print()
    print(colors("[*] help: print the help message.", "green"))
    print()
    print(colors("[*] exit/quit: Leave the program.", "green"))
    print()
    print(colors("[*] set: Set a variable's value: ", "green"))
    print()
    print(colors("[*] parameters: ", "red"))
    print()
    print(colors("   -- domain", "yellow"))
    print(colors("   -- target", "yellow"))
    print(colors("   -- port", "yellow"))
    print()
