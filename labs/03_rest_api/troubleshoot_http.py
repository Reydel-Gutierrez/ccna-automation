"""
Lab 03 — Troubleshoot HTTP responses using status, headers, and body.

Exam mapping: 2.5, 2.6

Run:
    python troubleshoot_http.py
"""

import requests


def diagnose(response: requests.Response, api_doc_expected: str) -> str:
    code = response.status_code
    if code == 401:
        return "Authentication failed. Check username/password, token, or API key."
    if code == 403:
        return "Authenticated but not authorized. The credential lacks permission."
    if code == 404:
        return f"Resource not found. Confirm the URL path. Docs expected: {api_doc_expected}"
    if code == 400:
        return "Bad request. Inspect JSON body/query params against the API schema."
    if code == 415:
        return "Unsupported media type. Set Content-Type to application/json (or yang-data+json)."
    if code == 429:
        retry = response.headers.get("Retry-After", "unknown")
        return f"Rate limited. Wait Retry-After={retry} seconds, then retry."
    if 500 <= code <= 599:
        return "Server-side failure. Retry later; do not assume your payload is wrong."
    if 200 <= code <= 299:
        return "Success. Parse the body."
    return f"Unexpected status {code}."


if __name__ == "__main__":
    cases = [
        ("https://httpbin.org/status/401", "/devices"),
        ("https://httpbin.org/status/404", "GET /organizations/{id}/devices"),
        ("https://httpbin.org/status/429", "GET /networks"),
        ("https://httpbin.org/status/200", "GET /get"),
    ]
    for url, expected in cases:
        r = requests.get(url, timeout=15)
        print(f"{r.status_code}: {diagnose(r, expected)}")
