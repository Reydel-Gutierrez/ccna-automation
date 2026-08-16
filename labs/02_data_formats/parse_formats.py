"""
Lab 02 — Parse XML, JSON, and YAML into Python data structures.

Exam mapping: 1.1, 1.2

Run from this folder:
    python parse_formats.py
"""

import json
from pathlib import Path
from xml.etree import ElementTree as ET

import yaml

HERE = Path(__file__).resolve().parent
NS = {"if": "urn:ietf:params:xml:ns:yang:ietf-interfaces"}


def parse_json(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["interfaces"]


def parse_yaml(path: Path) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data["interfaces"]


def parse_xml(path: Path) -> list[dict]:
    root = ET.parse(path).getroot()
    interfaces = []
    for iface in root.findall("if:interface", NS):
        interfaces.append(
            {
                "name": iface.findtext("if:name", default="", namespaces=NS),
                "description": iface.findtext("if:description", default="", namespaces=NS),
                "enabled": iface.findtext("if:enabled", default="", namespaces=NS) == "true",
                "ipv4": {
                    "address": iface.findtext("if:ipv4/if:address", default="", namespaces=NS),
                    "prefix": int(iface.findtext("if:ipv4/if:prefix", default="0", namespaces=NS)),
                },
            }
        )
    return interfaces


if __name__ == "__main__":
    json_ifaces = parse_json(HERE / "interfaces.json")
    yaml_ifaces = parse_yaml(HERE / "interfaces.yaml")
    xml_ifaces = parse_xml(HERE / "interfaces.xml")

    print("JSON type:", type(json_ifaces), "first name:", json_ifaces[0]["name"])
    print("YAML type:", type(yaml_ifaces), "first name:", yaml_ifaces[0]["name"])
    print("XML  type:", type(xml_ifaces), "first name:", xml_ifaces[0]["name"])
    print("All three agree:", json_ifaces == yaml_ifaces == xml_ifaces)
