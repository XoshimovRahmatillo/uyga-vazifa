with open("dars.txt", 'w+') as f:
    matn = input("Matn kiriting: ")
    f.write(''.join(reversed(matn)))

with open("misol5.txt", "r") as f:
    matn = f.read()
print(matn)