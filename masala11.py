fayl = input("fayl nomini kiriting: ")

try:
    with open(fayl, "r") as f:
        matn = f.read()
        print(matn)
except FileNotFoundError:
    print("fayl topilmadi")
