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
    msg = termcolor.colored(str(message), str(color), attrs=["bold"])
    return msg


def print_logo(version, author):
    banner = '''\n
        [ Linx - Penetration Testing Tools ]
        [ Author by {0} ]
        [ version {1} ]
    '''.format(author, version)
    return colors(banner, "blue")


def print_usage():
    ...
