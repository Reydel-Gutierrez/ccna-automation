import yaml

file = open("../yaml/interfaces.yaml")

data = yaml.safe_load(file)

print(type(data))