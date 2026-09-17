import xml.etree.ElementTree as ET

tree = ET.parse("../xml/interfaces.xml")
root = tree.getroot()

print(root.get("name"))
