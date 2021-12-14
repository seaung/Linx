from kamene.all import *
from lib.tools.utils import success, warning


def show_opt_sys(host):
    pkt = IP(dst=host)/ICMP()
    recv_pkt = sr1(pkt, timeout=1, verbose=0)
    if recv_pkt is None:
        print(warning("No responder."))
    elif int(recv_pkt[IP].ttl) <= 64:
        print(success("Linux/Unix system."))
    elif int(recv_pkt[IP].ttl) <= 128:
        print(success("Windows system."))
    else:
        print(warning("Unkown system."))
