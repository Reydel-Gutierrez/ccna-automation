devices = [
    {"hostname": "R1", "status": "up"},
    {"hostname": "R2", "status": "down"},
    {"hostname": "R3", "status": "up"},
    {"hostname": "R4", "status": "down"},
    {"hostname": "R5", "status": "up"},
    {"hostname": "R6", "status": "down"},
    {"hostname": "R7", "status": "up"},
    {"hostname": "R8", "status": "down"}
]

for device in devices:
    if device["status"] == "up":
        print(device["hostname"])



