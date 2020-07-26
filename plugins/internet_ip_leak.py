import re
import requests


_INNER_IPADDR = re.compile(r"\b((?:10\.\d|172\.(1[6-9]|2\d|3[0-1])|192\.168)(?:\.\d+){2})\b")


def audit(target_url: str):
    response = requests.get(url=target_url)
    if response and response.status_code == 200:
        inner_ipaddr = [for line in response.iter_lines() for match in _INNER_IPADDR.finditer(line) if all(0<=int(x)<=255) for x in match.group(1).split(".")]
        if inner_ipaddr:
            print("[+] Found Inner address")
