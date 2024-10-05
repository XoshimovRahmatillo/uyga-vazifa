def sozni_hisobla(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            matn = file.read()
            sozlar = matn.split()
            return len(sozlar)
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return 0
    except Exception as e:
        print(f"Xato: {e}")
        return 0

fayl_nomi = input("Fayl nomini kiriting: ")
soz_soni = sozni_hisobla(fayl_nomi)

print(f"Faylda {soz_soni} ta so'z bor.")