import re
import requests

_ROBOTS_RE = re.compile(r"(user-agent|disallow|allow)", re.I)


def audit(target_url: str):
    url = target_url + "/robots.txt"

    response = requests.get(url=url)

    if response and response.status_code == 200 and _ROBOTS_RE.search(response.text):
        print("[!] Found Robots file")
