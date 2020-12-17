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


def colors(message, color):
    msg = termcolor.colored(str(meesage), str(color), attrs=["bold"])
    return msg


def success(msg):
    print(termcolor.colored(str(msg), str("cyan"), attrs["bold"]))


def warning(msg):
    print(termcolor.colored(str(msg), str("yellow"), attrs=["bold"]))


def info(msg):
    print(termcolor.colored(str(msg), str("green"), attrs=["bold"]))


def error(msg):
    print(termcolor.colored(str(msg), str("red"), attrs=["bold"]))
