"""
Lab 06 — NETCONF <get-config> against Cisco IOS XE using ncclient.

Exam mapping: 3.8, 5.1, 5.10

NETCONF default port is 830/tcp over SSH. Payloads are XML RPCs.
"""

import os
import sys

from dotenv import load_dotenv
from ncclient import manager

load_dotenv()

FILTER = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
</filter>
"""


if __name__ == "__main__":
    host = os.getenv("IOSXE_HOST")
    port = int(os.getenv("IOSXE_NETCONF_PORT", "830"))
    user = os.getenv("IOSXE_USER")
    password = os.getenv("IOSXE_PASSWORD")
    if not all([host, user, password]):
        sys.exit("Set IOSXE_HOST, IOSXE_USER, IOSXE_PASSWORD in labs/.env")

    with manager.connect(
        host=host,
        port=port,
        username=user,
        password=password,
        hostkey_verify=False,
        device_params={"name": "iosxe"},
        allow_agent=False,
        look_for_keys=False,
    ) as m:
        print("Connected. Capabilities (first 8):")
        for cap in list(m.server_capabilities)[:8]:
            print(" ", cap)
        reply = m.get_config(source="running", filter=FILTER)
        print(reply.xml)
