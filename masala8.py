import json

with open("JSON.json", "r") as fayl:
    malumot = json.load(fayl)
malumot["Mashinalar"] = {
    "mashina": input("yoqtirgan mashinangizni kiriting: "),
    "rangi": input("Mashinangizni rangini kiriting: "),
    "narxi": int(input("Mashinangizni narxini kiriting: "))
}

with open("masala8.json", "w") as fayl:
    json.dump(malumot, fayl, indent=4)