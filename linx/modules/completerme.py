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
        self.commands = {
            'set': ['interface', 'domain', 'port', 'target', 'help'],
            'show': ['interface', 'domain', 'port', 'target', 'help'],
            'crawler': ['show', 'start'],
            'exploit': ['show', 'redis', 'mysql'],
            'scan': ['show', 'start'],
            'encoder': ['show', 'encode', 'decode'],
            'burp': ['show', 'db', 'ssh'],
            'sniffer': ['show', 'start'],
            'wifi': ['show', 'scan', 'crack', 'disconnect'],
            'rpc': ['show', 'server', 'connect', 'exec', 'upload', 'download']
        }
        self.base_commands = ['clear', 'help', 'exit', 'quit'] + list(self.commands.keys())
        
        if console == 'linx':
            history_path = '{0}.linx_history'.format(path)
            try:
                readline.read_history_file(history_path)
            except FileNotFoundError:
                pass
            readline.set_completer(self.linx)
            readline.set_completer_delims(' ')

    def linx(self, text: str, state: int) -> Any:
        buffer = readline.get_line_buffer()
        line = buffer.lstrip()
        tokens = line.split()

        # 如果是空行或者只有一个词的开始
        if not tokens or (len(tokens) == 1 and not line.endswith(' ')):
            results = [x for x in self.base_commands if x.startswith(text)] + [None]
            return results[state]

        # 如果是第二个或更多词
        cmd = tokens[0].lower()
        if cmd in self.commands:
            if len(tokens) == 1 or (len(tokens) == 2 and not line.endswith(' ')):
                results = [x for x in self.commands[cmd] if x.startswith(text)] + [None]
                return results[state]
            
            # 特殊命令的第三个参数补全
            if cmd == 'exploit' and len(tokens) >= 2:
                if tokens[1] == 'mysql' and (len(tokens) == 2 or (len(tokens) == 3 and not line.endswith(' '))):
                    return ['root', None][state]
            elif cmd == 'wifi' and len(tokens) >= 2:
                if tokens[1] == 'crack' and (len(tokens) == 2 or (len(tokens) == 3 and not line.endswith(' '))):
                    return ['<ssid>', None][state]

        return None

    def suboption(self, text: str, state: int) -> Any:
        results = [x for x in self.suboptions if x.startswith(text)] + [None]
        return results[state]

    def verify(self, text: str, state: int) -> Any:
        self.words = []
        results = [x for x in self.words if x.startswith(text)] + [None]
        return results[state]

