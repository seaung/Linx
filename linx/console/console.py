import os
import sys

import psutil
import termcolor
from modules.help import print_usage

from modules.helper import color
from modules.completerme import CompleterMe
from modules.crawler import CrawlerSpider


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

    def start(self) -> None:
        '''整个Linx程序的核心'''
        try:
            save_command_history("") # 创建.linx_history文件
            while True:
                completerme = CompleterMe(self.path, 'linx')
                console = termcolor.colored('linx> ', 'red', attrs=['bold'])

                try:
                    self.command = input('{}'.format(console))
                except EOFError:
                    self.command = 'exit'

                save_command_history(self.command)
                self.input_list = self.command.split()

                try:
                    # 处理clear命令
                    if self.command == 'clear' or self.command == 'CLEAR':
                        os.system('clear' if os.name == 'posix' else 'cls')
                        continue

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
                                    color('[+] Interface set to: {}'.format(self.interface), 'green')
                                except IndexError:
                                    try:
                                        self.interface = input('[+] Enter the interface :')
                                        if self.interface:
                                            color('[+] Interface set to: {}'.format(self.interface), 'green')
                                    except KeyboardInterrupt:
                                        pass
                            elif self.input_list[1] == 'domain':
                                try:
                                    self.domain = self.input_list[2]
                                    color('[+] Domain set to: {}'.format(self.domain), 'green')
                                except IndexError:
                                    try:
                                        self.domain = input('[+] Enter the domain :')
                                        if self.domain:
                                            color('[+] Domain set to: {}'.format(self.domain), 'green')
                                    except KeyboardInterrupt:
                                        pass
                            elif self.input_list[1] == 'port':
                                try:
                                    self.port = int(self.input_list[2])
                                    color('[+] Port set to: {}'.format(self.port), 'green')
                                except IndexError:
                                    try:
                                        self.port = input('[+] Enter the default port: ')
                                        if self.port:
                                            self.port = int(self.port)
                                            color('[+] Port set to: {}'.format(self.port), 'green')
                                    except KeyboardInterrupt:
                                        pass
                                except ValueError:
                                    color('[!] Port must be a number', 'red')
                            elif self.input_list[1] == 'target':
                                try:
                                    self.targets = self.input_list[2]
                                    color('[+] Target set to: {}'.format(self.targets), 'green')
                                except IndexError:
                                    try:
                                        self.targets = input('[+] Enter the target :')
                                        if self.targets:
                                            color('[+] Target set to: {}'.format(self.targets), 'green')
                                    except KeyboardInterrupt:
                                        pass
                            else:
                                color('[!] Invalid variable name. Available options: interface, target, domain, port','red')
                        except IndexError:
                            color('[!] Select a valid variable to set.', 'red')
                    elif self.input_list[0] == 'show' or self.input_list[0] == 'SHOW': # 显示设置的信息处理逻辑分支
                        try:
                            if self.input_list[1] == 'interface':
                                if self.interface:
                                    color('[*] Network interface: {}'.format(self.interface), 'green')
                                else:
                                    color('[!] Interface is not set', 'yellow')
                            elif self.input_list[1] == 'target':
                                if self.targets:
                                    color('[*] Target: {}'.format(self.targets), 'green')
                                else:
                                    color('[!] Target is not set', 'yellow')
                            elif self.input_list[1] == 'domain':
                                if self.domain:
                                    color('[*] Domain: {}'.format(self.domain), 'green')
                                else:
                                    color('[!] Domain is not set', 'yellow')
                            elif self.input_list[1] == 'port':
                                if self.port:
                                    color('[*] Port: {}'.format(self.port), 'green')
                                else:
                                    color('[!] Port is not set', 'yellow')
                            else:
                                color('[!] Invalid variable name. Available options: interface, target, domain, port', 'red')
                        except IndexError:
                            color('[!] Usage: show <variable>', 'red')
                    elif self.input_list[0] == 'crawler' or self.input_list[0] == 'CRAWLER': # 爬虫模块逻辑
                        if self.input_list[1] == 'show':
                            color('\n[Help] start a crawler in target URL.', 'green')
                            color('[Required] URL as target.', 'green')
                            color('For example:', 'green')
                            color('{} set target http://www.example.com'.format(console), 'green')
                            color('{} crawler start \n'.format(console), 'green')
                            continue
                        elif self.input_list[1] == 'start': # 开始爬取网站url
                            try:
                                if not self.targets:
                                    color('[!] Please set target first using "set target <url>"', 'red')
                                    continue
                                spider = CrawlerSpider()
                                spider.run(self.targets)
                            except KeyboardInterrupt:
                                pass
                            except Exception as e:
                                color('[!] Exception caught : {}'.format(e), 'yellow')
                    elif self.input_list[0] == 'exploit' or self.input_list[0] == 'Exploit': # 漏洞利用逻辑
                        try:
                            if self.input_list[1] == 'show':
                                color('\n[Help] Redis and MySQL remote command execution.', 'green')
                                color('[Required] Target host, port and command.', 'green')
                                color('For example:', 'green')
                                color('{} set domain example.com'.format(console), 'green')
                                color('{} set port 6379'.format(console), 'green')
                                color('{} exploit redis "INFO"'.format(console), 'green')
                                color('{} exploit mysql "root" "password" "SELECT VERSION();"\n'.format(console), 'green')
                                continue
                            elif len(self.input_list) >= 3:
                                if not self.domain:
                                    color('[!] Please set domain first using "set domain <domain>"', 'red')
                                    continue
                                from modules.exploit import Exploit
                                exploit = Exploit(self.domain, self.port)
                                
                                if self.input_list[1] == 'redis':
                                    command = ' '.join(self.input_list[2:])
                                    result = exploit.redis_rce(command)
                                    if result:
                                        color('\n[+] Redis command execution result:', 'green')
                                        color('[+] Command: {}'.format(command), 'green')
                                        color('[+] Output: {}\n'.format(result), 'green')
                                    else:
                                        color('\n[!] Failed to execute Redis command', 'red')
                                elif self.input_list[1] == 'mysql' and len(self.input_list) >= 4:
                                    user = self.input_list[2]
                                    password = self.input_list[3]
                                    command = ' '.join(self.input_list[4:])
                                    result = exploit.mysql_rce(user, password, command)
                                    if result:
                                        color('\n[+] MySQL command execution result:', 'green')
                                        color('[+] Command: {}'.format(command), 'green')
                                        color('[+] Output: {}\n'.format(result), 'green')
                                    else:
                                        color('\n[!] Failed to execute MySQL command', 'red')
                                else:
                                    color('[!] Invalid command format. Use "exploit show" for help.', 'red')
                            else:
                                color('[!] Invalid command format. Use "exploit show" for help.', 'red')
                        except Exception as e:
                            color('[!] Exception caught : {}'.format(e), 'yellow')
                            pass
                    elif self.input_list[0] == 'scan' or self.input_list[0] == 'SCAN': # 端口扫描逻辑
                        try:
                            if self.input_list[1] == 'show':
                                color('\n[Help] Scan ports on target host.', 'green')
                                color('[Required] Domain or IP address as target.', 'green')
                                color('For example:', 'green')
                                color('{} set domain example.com'.format(console), 'green')
                                color('{} scan start\n'.format(console), 'green')
                                continue
                            elif self.input_list[1] == 'start':
                                if not self.domain:
                                    color('[!] Please set domain first using "set domain <domain>"', 'red')
                                    continue
                                from modules.scan import Scanner
                                scanner = Scanner(self.domain)
                                open_ports = scanner.port_scan()
                                if open_ports:
                                    color('\n[*] Open ports on {}'.format(self.domain), 'green')
                                    for port, service in open_ports:
                                        color('[+] Port {} is open (Service: {})'.format(port, service), 'green')
                                else:
                                    color('\n[*] No open ports found on {}'.format(self.domain), 'yellow')
                        except IndexError:
                            color('[!] Invalid command format. Use "scan show" for help.', 'red')
                        except Exception as e:
                            color('[!] Exception caught : {}'.format(e), 'yellow')
                    elif self.input_list[0] == 'encoder' or self.input_list[0] == 'ENCODER': # 编码器处理逻辑
                        try:
                            if self.input_list[1] == 'show':
                                color('\n[Help] Text encoding and decoding tool.', 'green')
                                color('[Required] Text to encode/decode and method.', 'green')
                                color('Supported methods:', 'green')
                                color('  - encode: base64, url, html, md5, sha1, sha256, sha512', 'green')
                                color('  - decode: base64, url, html', 'green')
                                color('For example:', 'green')
                                color('{} encoder encode base64 "Hello World"'.format(console), 'green')
                                color('{} encoder decode base64 "SGVsbG8gV29ybGQ="\n'.format(console), 'green')
                                continue
                            elif len(self.input_list) >= 4 and self.input_list[1] in ['encode', 'decode']:
                                operation = self.input_list[1]
                                method = self.input_list[2]
                                text = ' '.join(self.input_list[3:])
                                
                                from modules.encoder import Encoder
                                encoder = Encoder()
                                
                                if operation == 'encode':
                                    result = encoder.encode(text, method)
                                else:
                                    result = encoder.decode(text, method)
                                    
                                if result:
                                    color('\n[+] {} result:'.format(operation.capitalize()), 'green')
                                    color('[+] Input text: {}'.format(text), 'green')
                                    color('[+] Method: {}'.format(method), 'green')
                                    color('[+] Output: {}\n'.format(result), 'green')
                                else:
                                    color('\n[!] Failed to {} text with method {}'.format(operation, method), 'red')
                            else:
                                color('[!] Invalid command format. Use "encoder show" for help.', 'red')
                        except Exception as e:
                            color('[!] Exception caught : {}'.format(e), 'yellow')
                            pass
                    elif self.input_list[0] == 'burp' or self.input_list[0] == 'BURP': # 爆破相关逻辑
                        try:
                            if self.input_list[1] == 'show':
                                color('\n[Help] Database and SSH brute force attack.', 'green')
                                color('[Required] Target host, port and wordlist file.', 'green')
                                color('For example:', 'green')
                                color('{} set domain example.com'.format(console), 'green')
                                color('{} set port 3306'.format(console), 'green')
                                color('{} burp db start /path/to/wordlist'.format(console), 'green')
                                color('{} burp ssh start /path/to/wordlist'.format(console), 'green')
                                continue
                            elif len(self.input_list) >= 4 and self.input_list[1] in ['db', 'ssh'] and self.input_list[2] == 'start':
                                if not self.domain:
                                    color('[!] Please set domain first using "set domain <domain>"', 'red')
                                    continue
                                wordlist = self.input_list[3]
                                if self.input_list[1] == 'db':
                                    from modules.db_burp import DBBurp
                                    burp = DBBurp(self.domain, wordlist, self.port)
                                    burp.run()
                                else:
                                    from modules.ssh_brup import SSHBrute
                                    burp = SSHBrute(self.domain, wordlist, self.port)
                                    burp.run()
                            else:
                                color('[!] Invalid command format. Use "burp show" for help.', 'red')
                        except Exception as e:
                            color('[!] Exception caught : {}'.format(e), 'yellow')
                            pass
                    elif self.input_list[0] == 'sniffer' or self.input_list[0] == 'SNIFFER': # 流量嗅探模块
                        try:
                            if self.input_list[1] == 'show':
                                color('\n[Help] Network traffic sniffer.', 'green')
                                color('[Required] Network interface to sniff on.', 'green')
                                color('For example:', 'green')
                                color('{} set interface eth0'.format(console), 'green')
                                color('{} sniffer start'.format(console), 'green')
                                continue
                            elif self.input_list[1] == 'start':
                                if not self.interface:
                                    color('[!] Please set interface first using "set interface <interface>"', 'red')
                                    continue
                                from modules.sniffer import Sniffer
                                sniffer = Sniffer(self.interface)
                                sniffer.start()
                            else:
                                color('[!] Invalid command format. Use "sniffer show" for help.', 'red')
                        except Exception as e:
                            color('[!] Exception caught : {}'.format(e), 'yellow')
                            pass
                    elif self.input_list[0] == 'wifi' or self.input_list[0] == 'WIFI': # wifi无线模块逻辑
                        try:
                            if self.input_list[1] == 'show':
                                color('\n[Help] WiFi network scanning and cracking.', 'green')
                                color('[Required] Network interface and wordlist file for cracking.', 'green')
                                color('For example:', 'green')
                                color('{} set interface en0'.format(console), 'green')
                                color('{} wifi scan'.format(console), 'green')
                                color('{} wifi crack <ssid> /path/to/wordlist'.format(console), 'green')
                                color('{} wifi disconnect\n'.format(console), 'green')
                                continue
                            elif self.input_list[1] == 'scan':
                                if not self.interface:
                                    color('[!] Please set interface first using "set interface <interface>"', 'red')
                                    continue
                                from modules.wifi import WiFiManager
                                wifi = WiFiManager(self.interface)
                                networks = wifi.scan_networks()
                                if networks:
                                    color('\n[*] Available WiFi networks:', 'green')
                                    for network in networks:
                                        color('[+] SSID: {} (Channel: {}, Security: {}, Signal: {})'.format(
                                            network['ssid'], network['channel'], network['security'], network['rssi']
                                        ), 'green')
                                else:
                                    color('\n[*] No WiFi networks found', 'yellow')
                            elif self.input_list[1] == 'crack':
                                if not self.interface:
                                    color('[!] Please set interface first using "set interface <interface>"', 'red')
                                    continue
                                if len(self.input_list) < 4:
                                    color('[!] Usage: wifi crack <ssid> <wordlist>', 'red')
                                    continue
                                ssid = self.input_list[2]
                                wordlist = self.input_list[3]
                                from modules.wifi import WiFiManager
                                wifi = WiFiManager(self.interface)
                                password = wifi.crack_network(ssid, wordlist)
                                if password:
                                    color('\n[+] Successfully cracked network!', 'green')
                                    color('[+] SSID: {}'.format(ssid), 'green')
                                    color('[+] Password: {}'.format(password), 'green')
                                    wifi.save_network_config(ssid, password)
                            elif self.input_list[1] == 'disconnect':
                                if not self.interface:
                                    color('[!] Please set interface first using "set interface <interface>"', 'red')
                                    continue
                                from modules.wifi import WiFiManager
                                wifi = WiFiManager(self.interface)
                                if wifi.disconnect():
                                    color('[+] Successfully disconnected from WiFi network', 'green')
                                else:
                                    color('[!] Failed to disconnect from WiFi network', 'red')
                            else:
                                color('[!] Invalid command format. Use "wifi show" for help.', 'red')
                        except IndexError:
                            color('[!] Invalid command format. Use "wifi show" for help.', 'red')
                        except Exception as e:
                            color('[!] Exception caught : {}'.format(e), 'yellow')
                            pass
                    elif self.input_list[0] == 'rpc' or self.input_list[0] == 'RPC': # 远程调用模块
                        try:
                            if self.input_list[1] == 'show':
                                color('\n[Help] Remote Procedure Call (RPC) module.', 'green')
                                color('[Required] Host and port for server/client.', 'green')
                                color('Commands:', 'green')
                                color('  - rpc server start : Start RPC server', 'green')
                                color('  - rpc connect <host> <port> : Connect to RPC server', 'green')
                                color('  - rpc exec <command> : Execute command on remote server', 'green')
                                color('  - rpc upload <local_file> <remote_file> : Upload file to server', 'green')
                                color('  - rpc download <remote_file> <local_file> : Download file from server\n', 'green')
                                continue
                            elif self.input_list[1] == 'server' and self.input_list[2] == 'start':
                                from modules.rpc import RPCServer
                                server = RPCServer('0.0.0.0', self.port)
                                try:
                                    server.start()
                                except KeyboardInterrupt:
                                    color('\n[*] RPC服务已停止', 'yellow')
                            elif self.input_list[1] == 'connect':
                                if len(self.input_list) < 4:
                                    color('[!] Usage: rpc connect <host> <port>', 'red')
                                    continue
                                host = self.input_list[2]
                                port = int(self.input_list[3])
                                from modules.rpc import RPCClient
                                self.rpc_client = RPCClient(host, port)
                                color('\n[*] 已连接到RPC服务器 {}:{}\n'.format(host, port), 'green')
                            elif self.input_list[1] == 'exec':
                                if not hasattr(self, 'rpc_client'):
                                    color('[!] 请先使用 rpc connect 连接到服务器', 'red')
                                    continue
                                if len(self.input_list) < 3:
                                    color('[!] Usage: rpc exec <command>', 'red')
                                    continue
                                command = ' '.join(self.input_list[2:])
                                result = self.rpc_client.execute_command(command)
                                if result:
                                    color('\n[+] 命令执行结果:', 'green')
                                    color(result, 'white')
                                else:
                                    color('\n[!] 命令执行失败', 'red')
                            elif self.input_list[1] == 'upload':
                                if not hasattr(self, 'rpc_client'):
                                    color('[!] 请先使用 rpc connect 连接到服务器', 'red')
                                    continue
                                if len(self.input_list) < 4:
                                    color('[!] Usage: rpc upload <local_file> <remote_file>', 'red')
                                    continue
                                local_file = self.input_list[2]
                                remote_file = self.input_list[3]
                                if self.rpc_client.upload_file(local_file, remote_file):
                                    color('\n[+] 文件上传成功', 'green')
                                else:
                                    color('\n[!] 文件上传失败', 'red')
                            elif self.input_list[1] == 'download':
                                if not hasattr(self, 'rpc_client'):
                                    color('[!] 请先使用 rpc connect 连接到服务器', 'red')
                                    continue
                                if len(self.input_list) < 4:
                                    color('[!] Usage: rpc download <remote_file> <local_file>', 'red')
                                    continue
                                remote_file = self.input_list[2]
                                local_file = self.input_list[3]
                                if self.rpc_client.download_file(remote_file, local_file):
                                    color('\n[+] 文件下载成功', 'green')
                                else:
                                    color('\n[!] 文件下载失败', 'red')
                            else:
                                color('[!] Invalid command format. Use "rpc show" for help.', 'red')
                        except IndexError:
                            color('[!] Invalid command format. Use "rpc show" for help.', 'red')
                        except Exception as e:
                            color('[!] Exception caught : {}'.format(e), 'yellow')
                            pass
                except KeyboardInterrupt:
                    sys.exit(1)

        except KeyboardInterrupt:
            color('[*] shutdown this program, bye!', 'green')
            sys.exit(1)
