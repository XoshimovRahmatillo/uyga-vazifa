def f(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            matn = file.read()
            sozlar = matn.split()

            if not sozlar:
                return None, None

            eng_uzun_soz = max(sozlar, key=len)
            eng_qisqa_soz = min(sozlar, key=len)

            return eng_uzun_soz, eng_qisqa_soz

    except FileNotFoundError:
        print("Fayl topilmadi.")
        return None, None
    except Exception as e:
        print(f"Xato: {e}")
        return None, None

fayl_nomi = input("Fayl nomini kiriting: ")
uzun_soz, qisqa_soz = f(fayl_nomi)

if uzun_soz and qisqa_soz:
    print(f"Eng uzun so'z: {uzun_soz}")
    print(f"Eng qisqa so'z: {qisqa_soz}")
else:
    print("Faylda so'zlar topilmadi.")