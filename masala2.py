matn=input("Matn kiriting: ")
ism=input("Fayl nomini kiriting: ")
f=open(f"{ism}",'w+')
f.write(f"{matn}")
f.seek(0)

for i in f.readlines():
    print(i,end=' ')

f.close()