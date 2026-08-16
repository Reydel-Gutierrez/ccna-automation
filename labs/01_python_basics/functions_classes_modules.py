"""
Lab 01 — Organize code into functions, classes, and modules.

Exam mapping: 1.5, 1.3, 4.5

Run:
    python functions_classes_modules.py
"""

from ipaddress import ip_network


def prefix_to_hosts(prefix: str) -> int:
    """Return usable host count for an IPv4 prefix. /31 and /32 are special."""
    net = ip_network(prefix, strict=False)
    if net.prefixlen >= 31:
        return net.num_addresses
    return net.num_addresses - 2


class Interface:
    """Minimal model of a network interface — Observer/MVC 'Model' idea."""

    def __init__(self, name: str, ip: str, enabled: bool = True):
        self.name = name
        self.ip = ip
        self.enabled = enabled

    def shutdown(self) -> None:
        self.enabled = False

    def summary(self) -> dict:
        return {"name": self.name, "ip": self.ip, "enabled": self.enabled}


def build_inventory(raw: list[dict]) -> list[Interface]:
    return [Interface(**item) for item in raw]


if __name__ == "__main__":
    print("Hosts in 192.168.10.0/24:", prefix_to_hosts("192.168.10.0/24"))
    print("Hosts in 10.0.0.1/32:", prefix_to_hosts("10.0.0.1/32"))

    inventory = build_inventory(
        [
            {"name": "GigabitEthernet1", "ip": "10.10.20.48/24"},
            {"name": "Loopback0", "ip": "192.0.2.1/32"},
        ]
    )
    inventory[0].shutdown()
    for iface in inventory:
        print(iface.summary())
