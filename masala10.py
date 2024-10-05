import json

with open("yosh_farqi.json", "r") as f:
    malumot = json.load(f)

yosh = [person["yosh"] for person in malumot]

maxs = max(yosh)
mins = min(yosh)

print(f"eng katta yosh: {maxs}")
print(f"eng kichik yosh: {mins}")