import json

 
with open("yosh.json", "r") as fayl:
    man = json.load(fayl)

 
yosh_18 = [person for person in man if person["yosh"] >= 18]


for i in yosh_18:
    print(f"Ism: {i['ism']},  Familiya: {i['familiya']},  Yosh: {i['yosh']}")
