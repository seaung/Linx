import termcolor

def colors(message, color):
    msg = termcolor.colored(str(message), str(color), attrs=["bold"])
    return msg

