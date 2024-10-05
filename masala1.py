matn=input("Matn kiriting: ")
f=open("Yangi matn fayli",'w+')
f.write(f"{matn}")
f.seek(0)

for i in f.readlines():
    print(i,end=' ')

f.close()