"""
Lab 03 — Construct REST requests with the Python requests library.

Exam mapping: 2.1, 2.4, 2.6, 2.7, 2.9

Uses httpbin.org so you can practice without Cisco credentials.
If httpbin is blocked, use https://jsonplaceholder.typicode.com/posts/1
"""

from pprint import pprint

import requests


BASE = "https://httpbin.org"


def show_response(label: str, response: requests.Response) -> None:
    print(f"\n=== {label} ===")
    print("URL:", response.url)
    print("Status:", response.status_code, response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))
    try:
        pprint(response.json())
    except ValueError:
        print(response.text[:400])


def get_with_query() -> None:
    # GET + query string. REST read operation.
    r = requests.get(f"{BASE}/get", params={"device": "csr1kv", "vrf": "mgmt"}, timeout=15)
    show_response("GET with query params", r)


def post_json() -> None:
    payload = {"hostname": "edge-01", "role": "wan"}
    r = requests.post(f"{BASE}/post", json=payload, timeout=15)
    show_response("POST JSON body", r)


def basic_auth() -> None:
    r = requests.get(f"{BASE}/basic-auth/admin/s3cret", auth=("admin", "s3cret"), timeout=15)
    show_response("HTTP Basic Auth", r)


def api_key_header() -> None:
    headers = {"X-Cisco-Meraki-API-Key": "fake-key-for-lab", "Accept": "application/json"}
    r = requests.get(f"{BASE}/headers", headers=headers, timeout=15)
    show_response("Custom API-key header", r)


def bearer_token() -> None:
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.lab"}
    r = requests.get(f"{BASE}/bearer", headers=headers, timeout=15)
    show_response("Bearer token", r)


def status_codes() -> None:
    for code in (200, 201, 400, 401, 403, 404, 429, 500):
        r = requests.get(f"{BASE}/status/{code}", timeout=15)
        print(f"Requested {code:>3} -> got {r.status_code} {r.reason}")


if __name__ == "__main__":
    get_with_query()
    post_json()
    basic_auth()
    api_key_header()
    bearer_token()
    print("\n=== Status code lab ===")
    status_codes()
