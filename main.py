import json

with open("agentsettings.json", "r") as json_file:
    agentsettings = json.load(json_file)

for i in agentsettings:
    options = agentsettings[i]
    for j in options:
        if j == "key":
            print(j, " - ", options[j])
        elif j == "group":
            # loop -> 차례로 입력
            print(j, " - ", options[j])
        elif j == "description":
            # loop -> 차례로 입력
            print(j, " - ", options[j])
        elif j == "badge":
            # loop -> 차례로 입력
            print(j, " - ", options[j])
        elif j == "defaultValue":
            print(j, " - ", options[j])
        elif j == "type":
            print(j, " - ", options[j])
        elif j == "unit":
            print(j, " - ", options[j])
