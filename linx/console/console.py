import os
import sys

import psutil
import termcolor
from linx.modules.help import print_usage

from modules.helper import color
from modules.completerme import CompleterMe


def save_command_history(command: str) -> None:
    '''保存命令行历史记录'''
    try:
        with open('.linx_history', 'a+') as fs:
            fs.write('{}\n'.format(command))
    except Exception as e:
        color('[!] Exception caught : {}'.format(e), 'red')
        pass


class ProcessConsole(object):
    '''程序核心类
    专门处理命令行控制台的输入输出操作
    '''
    name = 'process console'
    desc = 'console to process commands'
    version = '1.0.0'

    def __init__(self) -> None:
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))

        self.interface = None
        self.targets = None
        self.domain = None
        self.port = 135

    def pskill(self, pid: int) -> None:
        '''结束当前控制台进程'''
        process = psutil.Process(pid)
        for item in process.children(recursive=True):
            item.kill()
        process.kill()

    def start(self):
        try:
            save_command_history("") # 创建.linx_history文件
            while True:
                completerme = CompleterMe(self.path, 'linx')
                console = termcolor.colored('linx>', 'red', attrs=['bold'])

                try:
                    self.command = input('{}'.format(console))
                except EOFError:
                    self.command = 'exit'

                save_command_history(self.command)
                self.input_list = self.command.split()

                try:
                    # 帮助信息逻辑
                    if self.command == 'help' or self.command == 'HELP': # 输出帮助信息
                        print_usage()
                    # 程序推出逻辑
                    elif self.command == 'exit' or self.command == 'quit': # 推出程序
                        color('[*] shutdown this program, bye!', 'green')
                        sys.exit(1)
                    # 设置变量逻辑
                    elif self.input_list[0] == 'set' or self.input_list[0] == 'SET': # 这个分支用来设置变量
                        try:
                            if self.input_list[1] == 'interface':
                                try:
                                    self.interface = self.input_list[2]
                                except IndexError:
                                    try:
                                        self.interface = input('[+] Enter the interface :')
                                    except KeyboardInterrupt:
                                        pass
                            elif self.input_list[1] == 'domain':
                                try:
                                    self.domain = self.input_list[2]
                                except IndexError:
                                    try:
                                        self.domain = input('[+] Enter the domain :')
                                    except KeyboardInterrupt:
                                        pass
                            elif self.input_list[1] == 'port':
                                try:
                                    self.port = int(self.input_list[2])
                                except IndexError:
                                    try:
                                        self.port = input('[+] Enter the default port: ')
                                    except KeyboardInterrupt:
                                        pass
                        except IndexError:
                            color('[!] Select a valid variable to set.', 'red')
                    elif self.input_list[0] == 'show' or self.input_list[0] == 'SHOW': # 显示设置的信息处理逻辑分支
                        try:
                            if self.input_list[1] == 'interface':
                                color('[*] Network interface : {}'.format(self.interface), 'green')
                            elif self.input_list[1] == 'target':
                                color('[*] Target(s) : {}'.format(self.targets), 'green')
                            elif self.input_list[1] == 'domain':
                                color('[*] Domain : {}'.format(self.domain), 'green')
                            elif self.input_list[1] == 'port':
                                color('[*] Port : {}'.format(self.port), 'green')
                        except IndexError:
                            color('[!] Select a valid variable name.', 'red')
                    elif self.input_list[0] == 'crawler' or self.input_list[0] == 'CRAWLER': # 爬虫模块逻辑
                        if self.input_list[0] == 'show':
                            color('\n[Help] start a crawler in target URL.', 'green')
                            color('[Required] URL as target.', 'green')
                            color('For example:', 'green')
                            color('{} set target http://www.example.com'.format(console), 'green')
                            color('{} crawler start \n'.format(console), 'green')
                            continue
                        elif self.input_list[0] == 'start': # 开始爬取网站url
                            try:
                                pass
                            except KeyboardInterrupt:
                                pass
                            except Exception as e:
                                color('[!] Exception caught : {}'.format(e), 'yellow')
                    elif self.input_list[0] == 'exploit' or self.input_list[0] == 'Exploit': # 漏洞利用逻辑
                        try:
                            pass
                        except IndexError:
                            pass
                        except TypeError:
                            pass
                        except KeyboardInterrupt:
                            pass
                        except Exception as e:
                            color('[!] Exception caught : {}'.format(e), 'yellow')
                            pass
                    elif self.input_list[0] == 'scan' or self.input_list[0] == 'SCAN': # 端口扫描逻辑
                        try:
                            pass
                        except IndexError:
                            pass
                        except TypeError:
                            pass
                        except KeyboardInterrupt:
                            pass
                        except Exception as e:
                            color('[!] Exception caught : {}'.format(e), 'yellow')
                            pass
                    elif self.input_list[0] == 'encoder' or self.input_list[0] == 'ENCODER': # 编码器处理逻辑
                        try:
                            pass
                        except IndexError:
                            pass
                        except TypeError:
                            pass
                        except KeyboardInterrupt:
                            pass
                        except Exception as e:
                            color('[!] Exception caught : {}'.format(e), 'yellow')
                            pass
                except KeyboardInterrupt:
                    sys.exit(1)

        except KeyboardInterrupt:
            color('[*] shutdown this program, bye!', 'green')
            sys.exit(1)
