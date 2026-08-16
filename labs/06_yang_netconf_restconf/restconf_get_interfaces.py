"""
Lab 06 — RESTCONF GET against Cisco IOS XE.

Exam mapping: 3.6, 3.8, 5.10

1. Open https://devnetsandbox.cisco.com
2. Launch IOS XE on Catalyst 8000 (Always-On) or a reservable IOS XE lab.
3. Copy host, RESTCONF port, username, and password into labs/.env
4. Run: python restconf_get_interfaces.py

RESTCONF uses HTTPS (usually TCP 443) and YANG-identified URLs.
NETCONF uses SSH (TCP 830) and XML RPCs — see netconf_get_config.py
"""

import os
import sys
from pprint import pprint

import requests
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
load_dotenv()

HOST = os.getenv("IOSXE_HOST")
PORT = os.getenv("IOSXE_RESTCONF_PORT", "443")
USER = os.getenv("IOSXE_USER")
PASSWORD = os.getenv("IOSXE_PASSWORD")

HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def restconf(path: str):
    url = f"https://{HOST}:{PORT}/restconf/data/{path}"
    r = requests.get(url, auth=(USER, PASSWORD), headers=HEADERS, verify=False, timeout=30)
    print(f"GET {url}")
    print("Status:", r.status_code)
    print("Content-Type:", r.headers.get("Content-Type"))
    if r.status_code >= 400:
        print(r.text[:800])
        r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    if not all([HOST, USER, PASSWORD]):
        sys.exit("Set IOSXE_HOST, IOSXE_USER, IOSXE_PASSWORD in labs/.env")

    hostname = restconf("Cisco-IOS-XE-native:native/hostname")
    pprint(hostname)

    interfaces = restconf("ietf-interfaces:interfaces")
    pprint(interfaces)
