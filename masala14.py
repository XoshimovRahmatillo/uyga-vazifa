a,b=map(int,input("boshlanish va tugashni kiriting: ").split())
son = float(input("sonlarni kiriting: "))
if son < a or son > b:
    raise Exception(f"son {a} dan {b} orasida bolish kerak")
print("Son tog'ri tanlandi tabriklaymiz!")