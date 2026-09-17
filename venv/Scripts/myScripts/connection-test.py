import requests

url = "https://sandbox-iosxe-recomm-1.cisco.com"
auth = ("developer", "C1sco12345")

r = requests.get(
    url + "/restconf/data/ietf-interfaces:interfaces",
    auth=auth,
    headers={"Accept": "application/yang-data+json"},
    verify=False
)

print(r.status_code)
print(r.text)