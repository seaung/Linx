import sys
import time
import readline

from subprocess import *
from typing import Any


class CompleterMe(object):
    name = 'TAB completer'
    desc = 'Auto complete linx command with tab'
    version = '1.0.0'

    def __init__(self, path: str, console: str):
        tab = readline.parse_and_bind('tab: complete')
        if console == 'linx':
            history_path = '{0}.linx_history'.format(path)
            readline.read_history_file(history_path)
            completer = readline.set_completer(self.linx)

    def linx(self, text: str, state: int) -> Any:
        if 'set' in text and state == 1:
            self.suboptions = ['target', 'domain', 'port', 'help']
            completer = readline.set_completer(self.suboption)
        if 'print' in text and state == 1:
            self.suboptions = ['target', 'domain', 'port', 'help']
            completer = readline.set_completer(self.suboption)
        else:
            self.words = ['clear', 'help', 'exit']
            results = [x for x in self.words if x.startswith(text)] + [None]
            return results[state]

    def suboption(self, text: str, state: int) -> Any:
        results = [x for x in self.suboptions if x.startswith(text)] + [None]
        return results[state]

    def verify(self, text: str, state: int) -> Any:
        self.words = []
        results = [x for x in self.words if x.startswith(text)] + [None]
        return results[state]

