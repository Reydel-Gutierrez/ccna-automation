# import json

# file = open("../json/interfaces.json")

# data = json.load(file)

# Print the entire JSON prettified.

# print(json.dumps(data, indent=4))

# Print only CORE-RTR-01.

# print(data["CORE-RTR-01"])

# Print only Device_Information.

# print(data["CORE-RTR-01"]["Device_Information"])

# Print the router OS.

# print(data["CORE-RTR-01"]["Device_Information"]["OS"])

# Print the router location.

# print(data["CORE-RTR-01"]["Device_Information"]["Location"])

# Print the entire interfaces list.

# print(data["CORE-RTR-01"]["interfaces"])

# Print only the first interface.

# print(data["CORE-RTR-01"]["interfaces"][0])

# Print the name of the first interface.

# print(data["CORE-RTR-01"]["interfaces"][0]["name"])

# Print the IP of the second interface.

# print(data["CORE-RTR-01"]["interfaces"][1]["IP_address"])

# Print whether GigabitEthernet3 is enabled.

# print(data["CORE-RTR-01"]["interfaces"][2]["enabled"])

# Print the first DNS server.

# print(data["CORE-RTR-01"]["DNS"][0])

# Print the second protocol configured on GigabitEthernet2.

# print(data["CORE-RTR-01"]["interfaces"][1]["protocols"][1])

# Then loops 

# for i in data["CORE-RTR-01"]["interfaces"]:
#   print(i["name"])

# modify

# for i in data["CORE-RTR-01"]["interfaces"]:
#   print(i["name"], "-", i["IP_address"])

# enable?

# for i in data["CORE-RTR-01"]["interfaces"]:

#   if i["enabled"] :
#     enabled = "ENABLED"
#   else:
#     enabled = "DISABLED"
    
#   print(i["name"], "is", enabled)


import json

file = open("../json/datacenter.json")

data = json.load(file)

# Pretty-print the entire JSON.

# print(json.dumps(data, indent=4))

# Print DC-MIAMI's active status.

# print(data["DC-MIAMI"]["active"])

# Print the name of the second VLAN.

# print(data["DC-MIAMI"]["vlans"][1]["name"])

# Print the second subnet of the first VLAN.

# print(data["DC-MIAMI"]["vlans"][0]["subnets"][1])

# Print the first management protocol.

# print(data["DC-MIAMI"]["management"]["protocols"][0])

#loop
# for vlansIterator in data["DC-MIAMI"]["vlans"]:
#   print("VLAN", vlansIterator["id"], "-", vlansIterator["name"])

#anotherloop
# def subnetsCount(vlanSubnets):
#   counter = 0
#   for count in vlanSubnets:
#     counter = counter + 1

#   return counter

for vlansIterator in data["DC-MIAMI"]["vlans"]:
  print(vlansIterator["name"], "has", len(vlansIterator["subnets"]), "subnet(s)")