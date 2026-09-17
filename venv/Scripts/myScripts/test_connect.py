import requests
import urllib3

# Suppress SSL warnings for sandbox only
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = "devnetsandboxiosxec8k.cisco.com"
username = "YOUR_SANDBOX_USERNAME"
password = "YOUR_SANDBOX_PASSWORD"

url = f"https://{host}/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Accept": "application/yang-data+json"
}

response = requests.get(
    url,
    auth=(username, password),
    headers=headers,
    verify=False
)

print("Status code:", response.status_code)

if response.status_code == 200:

    print("SUCCESS — connected to Cisco RESTCONF!")

    response_data = response.json()

    interfaces = response_data["ietf-interfaces:interfaces"]["interface"]

    for interface in interfaces:

        ipv4 = interface.get("ietf-ip:ipv4", {})
        addresses = ipv4.get("address", [])

        if addresses:
            print(
                interface["name"],
                addresses[0]["ip"]
            )
        else:
            print(
                interface["name"],
                "No IP"
            )

else:

    print("RESTCONF request failed.")
    print(response.text)