from kamene.all import *
from lib.tools.utils import success, warning


def show_opt_sys(host):
    pkt = IP(dst=host)/ICMP()
    recv_pkt = sr1(pkt, timeout=1, verbose=0)
    if recv_pkt == None:
        print(warning("Lins > No responder."))
    elif int(recv_pkt[IP].ttl) <= 64:
        print(success("Lins > Linux/Unix system."))
    elif int(recv_pkt[IP].ttl) <= 128:
        print(success("Lins > Windows system."))
    else:
        print(warning("Lins > Unkown system."))
