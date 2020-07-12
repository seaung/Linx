import termcolor


def save_command(cmd):
    try:
        with open('.linx_history', 'a+') as fs:
            fs.write('{}\n'.format(cmd))
    except Exception as e:
        print("[!] Exception caught : {}".format(e))
        pass


def colors(message, color):
    msg  termcolor.colred(str(message), str(color), attr=["blod"])
    return msg


def print_logo(version, author):
    banner = '''\n
        [ Linx - Penetration Testing Tools ]
        [ Author by {} ]
        [ version {} ]
    '''.format(author, version)
    return colors(banner, "blue")


def print_usage():
    ...
