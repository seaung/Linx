import sys
import time
import readline
import subprocess


class Completer(object):
    def __init__(self, path, console):
        tab = readline.parse_and_bind("tab: complete")
        if console == "Linx":
            history_path = ".linx_history".format(path)
            readline.read_history_file(history_path)
            completer = readline.set_completer(self.linx)

        if console == "exploit":
            completer = readline.set_completer(self.exploit)

    def suboption(self, text, state):
        result = [x for x in self.suboptions if x.startswith(text)] + [None]
        return result[state]

    def exploit(self, text, state):
        self.completer_words = ['clear', 'help', 'exit', 'quit', 'print', 'set', 'break', 'run', 'exploit']
        result = [x for x in self.completer_words if x.startswith(text)] + [None]
        return result[state]

    def linx(self, text, state):
        if "set" in text and state == 1:
            self.suboptions = ['target', 'file', 'domain', 'port', 'help']
            completer = readline.set_completer(self.suboption)
        elif "print" in text and state == 1:
            self.suboptions = ['target', 'file', 'domain', 'port', 'help']
            completer = readline.set_completer(self.suboptions)
        elif "crawler" in text and state == 1:
            self.suboptions = ['start', 'help']
            completer = readline.set_completer(self.suboptions)
        else:
            self.completer_words = ['clear', 'help', 'crawler', 'set', 'print', 'exit', 'quit']
            result = [x for x in self.completer_words if x.startswith(text)] + [None]
            return result[state]
