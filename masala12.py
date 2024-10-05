malumot = {
    "rusm":"Mers",
    "rangi":"Qop-qora",
    "narxi":120000
}
kalit = input("kalitni kiriting: ")

try:
    qiymat = malumot[kalit]
    print(f"{kalit} : {qiymat}")
except KeyError:
   
    print(f"{kalit} kalitda mavjud emas.")