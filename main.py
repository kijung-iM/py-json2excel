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
            print("group:")
            groups = options[j]
            for k in groups:
                print("\t", k)
        elif j == "description":
            # loop -> 차례로 입력
            languages = options[j]
            print("languages:")
            for lang in languages:
                print(lang, " - ", languages[lang])
        elif j == "badge":
            # loop -> 차례로 입력
            print("badge:")
            badges = options[j]
            for badge in badges:
                print("\t", badge, " : ", badges[badge])
        elif j == "defaultValue":
            print(j, " - ", options[j])
        elif j == "type":
            print(j, " - ", options[j])
        elif j == "unit":
            print(j, " - ", options[j])
    print("==================================")
