sonlar = list(map(int, input("sonlarni kiriting:  ").split()))
for i in range(1, len(sonlar)):
    assert sonlar[i] > sonlar[i - 1], "sonlar o'sish tartibida emas."
print("o'sish tartibida")