from scapy.all import sniff, IP, TCP, UDP, ICMP

class Sniffer(object):
    def __init__(self, interface: str, filter: str) -> None:
        self.interface = interface
        self.filter = filter

    def packet_callback(self, packet) -> None:
        '''处理捕获到的数据包'''
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            proto = packet[IP].proto

            print(f"\n[+] IP数据包: {ip_src} -> {ip_dst}")

            if TCP in packet:
                sport = packet[TCP].sport
                dport = packet[TCP].dport
                print(f"[+] TCP {ip_src}:{sport} -> {ip_dst}:{dport}")
            
            elif UDP in packet:
                sport = packet[UDP].sport
                dport = packet[UDP].dport
                print(f"[+] UDP {ip_src}:{sport} -> {ip_dst}:{dport}")
            
            elif ICMP in packet:
                print(f"[+] ICMP {ip_src} -> {ip_dst}")

    def run(self) -> None:
        '''开始嗅探数据包'''
        try:
            print(f"[*] 开始在接口 {self.interface} 上嗅探数据包...")
            print(f"[*] 使用过滤器: {self.filter}")
            sniff(
                iface=self.interface,
                filter=self.filter,
                prn=self.packet_callback
            )
        except KeyboardInterrupt:
            print("\n[!] 停止嗅探...")
        except Exception as e:
            print(f"\n[!] 发生错误: {str(e)}")

