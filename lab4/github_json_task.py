print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

import json

with open("lab4/sample-data1.json", "r") as file:
    data = json.load(file)
    for item in data['imdata'][:3]:
        print(f"{item['l1PhysIf']['attributes']['dn']}                              {item['l1PhysIf']['attributes']['speed']}   {item['l1PhysIf']['attributes']['mtu']}")
