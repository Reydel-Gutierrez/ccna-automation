"""
Lab 05 — Catalyst Center: token auth, list network devices, list clients.

Exam mapping: 2.7, 3.2, 3.9.a, 3.9.c

Launch a Catalyst Center sandbox from https://devnetsandbox.cisco.com
and copy host/user/password into labs/.env

Older docs still say "DNA Center". The product is Cisco Catalyst Center.
Many URLs still contain /dna/.
"""

import os
import sys

import requests
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
load_dotenv()

HOST = os.getenv("CATALYST_CENTER_HOST")
USER = os.getenv("CATALYST_CENTER_USER")
PASSWORD = os.getenv("CATALYST_CENTER_PASSWORD")


def token() -> str:
    url = f"https://{HOST}/dna/system/api/v1/auth/token"
    r = requests.post(url, auth=(USER, PASSWORD), verify=False, timeout=30)
    print(f"POST {url} -> {r.status_code}")
    r.raise_for_status()
    return r.json()["Token"]


def get(path: str, tok: str):
    url = f"https://{HOST}{path}"
    r = requests.get(
        url,
        headers={"X-Auth-Token": tok, "Accept": "application/json"},
        verify=False,
        timeout=30,
    )
    print(f"GET {url} -> {r.status_code}")
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    if not all([HOST, USER, PASSWORD]):
        sys.exit("Set CATALYST_CENTER_HOST/USER/PASSWORD in labs/.env")

    tok = token()
    devices = get("/dna/intent/api/v1/network-device", tok)
    rows = devices.get("response", devices)
    print(f"Devices: {len(rows)}")
    for d in rows[:10]:
        print(" -", d.get("hostname"), d.get("managementIpAddress"), d.get("softwareType"))

    # Client/host inventory. Endpoint names vary by version; print status if 404.
    for path in (
        "/dna/intent/api/v1/client-health",
        "/dna/data/api/v1/clients",
    ):
        try:
            payload = get(path, tok)
            print("Clients payload keys:", list(payload)[:8])
            break
        except requests.HTTPError as exc:
            print("Not available:", path, exc)
