"""
Lab 05 — Meraki: obtain a list of devices (exam 3.9.a) and clients (3.9.c).

Requires a Dashboard API key. Prefer your own non-production org, or the
DevNet Meraki sandbox when it is listed at https://devnetsandbox.cisco.com

Never hard-code the key. Use labs/.env
"""

import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

BASE = os.getenv("MERAKI_BASE", "https://api.meraki.com/api/v1")
API_KEY = os.getenv("MERAKI_API_KEY")


def headers() -> dict:
    return {
        "X-Cisco-Meraki-API-Key": API_KEY,
        "Accept": "application/json",
    }


def get(path: str, params: dict | None = None):
    url = f"{BASE}{path}"
    r = requests.get(url, headers=headers(), params=params, timeout=30)
    print(f"GET {url} -> {r.status_code}")
    if r.status_code >= 400:
        print(r.text)
        r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    if not API_KEY:
        sys.exit("Set MERAKI_API_KEY in labs/.env")

    orgs = get("/organizations")
    org_id = orgs[0]["id"]
    print("Organization:", orgs[0]["name"], org_id)

    devices = get(f"/organizations/{org_id}/devices")
    print(f"Devices: {len(devices)}")
    for d in devices[:10]:
        print(" -", d.get("name"), d.get("model"), d.get("serial"), d.get("lanIp"))

    networks = get(f"/organizations/{org_id}/networks")
    if networks:
        net_id = networks[0]["id"]
        clients = get(f"/networks/{net_id}/clients", params={"timespan": 86400})
        print(f"Clients seen on {networks[0]['name']}: {len(clients)}")
        for c in clients[:10]:
            print(" -", c.get("description") or c.get("mac"), c.get("ip"), c.get("ssid"))
