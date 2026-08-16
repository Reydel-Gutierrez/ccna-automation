"""
Lab 10 — Map application connectivity failures to likely causes.

Exam mapping: 6.8, 6.9, 4.9
"""

from dataclasses import dataclass


@dataclass
class Symptom:
    description: str
    likely_cause: str
    first_check: str


CASES = [
    Symptom(
        "Browser reaches the VIP but the app sees the load-balancer IP as client IP",
        "NAT / SNAT on the load balancer or firewall",
        "Compare source IP in app logs with the real client; check X-Forwarded-For",
    ),
    Symptom(
        "TCP SYN is sent, no SYN-ACK. Packet capture shows no return traffic",
        "Transport port blocked by firewall or security group",
        "Confirm destination port (80/443/830) is allowed in both directions",
    ),
    Symptom(
        "Works off-network, fails on corporate Wi-Fi. TLS handshake to api.example.com stalls",
        "HTTP/HTTPS proxy intercept or missing proxy config",
        "Check HTTPS_PROXY/HTTP_PROXY and corporate SSL inspection trust store",
    ),
    Symptom(
        "Site-to-site users cannot reach 10.10.20.0/24. Local LAN uses the same prefix",
        "VPN overlap / interesting-traffic ACL",
        "Inspect local and remote proxy IDs / encryption domains for overlapping subnets",
    ),
]


if __name__ == "__main__":
    for i, case in enumerate(CASES, 1):
        print(f"{i}. Symptom: {case.description}")
        print(f"   Cause:    {case.likely_cause}")
        print(f"   Check:    {case.first_check}\n")
