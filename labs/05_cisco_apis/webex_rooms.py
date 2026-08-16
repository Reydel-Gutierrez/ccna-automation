"""
Lab 05 — Webex: manage spaces (rooms), participants, and messages.

Exam mapping: 3.4, 3.9.b, 2.2 (webhooks are related)

Create a free Webex account and a Bot or personal access token:
https://developer.webex.com/docs/getting-started
"""

import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

BASE = os.getenv("WEBEX_BASE", "https://webexapis.com/v1")
TOKEN = os.getenv("WEBEX_TOKEN")


def api(method: str, path: str, **kwargs):
    r = requests.request(
        method,
        f"{BASE}{path}",
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
        timeout=30,
        **kwargs,
    )
    print(f"{method} {path} -> {r.status_code}")
    if r.status_code >= 400:
        print(r.text)
        r.raise_for_status()
    return r.json() if r.text else {}


if __name__ == "__main__":
    if not TOKEN:
        sys.exit("Set WEBEX_TOKEN in labs/.env")

    me = api("GET", "/people/me")
    print("Authenticated as:", me.get("displayName"), me.get("emails"))

    room = api("POST", "/rooms", json={"title": "CCNAAUTO lab space"})
    room_id = room["id"]
    print("Created space:", room["title"], room_id)

    api("POST", "/messages", json={"roomId": room_id, "text": "Hello from the 200-901 lab"})
    messages = api("GET", "/messages", params={"roomId": room_id})
    print("Messages:", [m.get("text") for m in messages.get("items", [])])

    memberships = api("GET", "/memberships", params={"roomId": room_id})
    print("Participants:", [m.get("personEmail") for m in memberships.get("items", [])])

    # Cleanup so repeated labs do not clutter Webex
    api("DELETE", f"/rooms/{room_id}")
    print("Deleted lab space")
