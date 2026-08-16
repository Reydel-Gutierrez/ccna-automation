"""
Lab 01 — Construct a Python unit test (exam 4.5) and TDD (exam 1.3).

TDD cycle for this file:
    1. Write the tests first (they fail).
    2. Implement prefix_to_hosts until tests pass.
    3. Refactor without changing behavior.

Run:
    python -m unittest labs.01_python_basics.test_subnet
    python -m unittest test_subnet.py
"""

import unittest
from functions_classes_modules import prefix_to_hosts


class TestPrefixToHosts(unittest.TestCase):
    def test_slash_24(self):
        self.assertEqual(prefix_to_hosts("192.168.1.0/24"), 254)

    def test_slash_30(self):
        self.assertEqual(prefix_to_hosts("10.0.0.0/30"), 2)

    def test_slash_32(self):
        self.assertEqual(prefix_to_hosts("172.16.0.1/32"), 1)

    def test_invalid_raises(self):
        with self.assertRaises(ValueError):
            prefix_to_hosts("not-an-ip")


if __name__ == "__main__":
    unittest.main()
