"""
Lab 05 — Interpret an SDK-style wrapper around REST (exam 3.1).

This is a tiny local SDK so you can practice reading SDK docs and calling
methods without depending on a Cisco package that may change. Compare this
pattern to meraki, dnacentersdk, or webexpythonsdk.
"""

from dataclasses import dataclass

import requests


@dataclass
class FakeCiscoSDK:
    base_url: str
    token: str
    verify: bool = True

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.token}", "Accept": "application/json"}

    def get_devices(self) -> list[dict]:
        r = requests.get(f"{self.base_url}/devices", headers=self._headers(), timeout=15, verify=self.verify)
        r.raise_for_status()
        return r.json()


if __name__ == "__main__":
    # httpbin echoes the request; this shows SDK wrapping, not a live inventory.
    sdk = FakeCiscoSDK(base_url="https://httpbin.org", token="lab-token")
    r = requests.get("https://httpbin.org/headers", headers=sdk._headers(), timeout=15)
    print("SDK would send headers:")
    print(r.json()["headers"])
