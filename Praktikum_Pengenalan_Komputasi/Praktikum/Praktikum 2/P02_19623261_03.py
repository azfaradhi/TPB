# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal: 5 Oktober 2023
# Deskripsi: Menentukan siapa yang akan memenangkan pertandingan

# Kamus:
# role_pemain1,role_pemain2: string
# HP_pemain1, HP_pemain2 : Float
# ATK_point1, ATK_point2 : Int
# Cek: Boolean
# count1, count2 : int

# Algoritma:

# Input:

role_pemain1 = input("Masukkan role pemain 1: ")

if role_pemain1 == "warrior":
    ATK_point1 = 10
    HP_pemain1 = float(input(f"Masukan sisa HP {role_pemain1} (P1): "))
    if HP_pemain1 > 100 or HP_pemain1 < 0:
        cek = False
        while (HP_pemain1 > 100 or HP_pemain1 < 0) and cek == False:
            print("HP tidak Valid!")
            HP_pemain1 = float(input(f"Masukan sisa HP {role_pemain1} (P1): "))
            if 0 <= HP_pemain1 <= 100:
                cek = True
    
    role_pemain2 = input("Masukkan role pemain 2: ")

    if role_pemain2 == "warrior":
        HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
        ATK_point2 = 10
        if HP_pemain2 > 100 or HP_pemain2 < 0:
            cek = False
            while (HP_pemain2> 100 or HP_pemain2 < 0) and cek == False:
                print("HP tidak Valid!")
                HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
                if 0 <= HP_pemain2 <= 100:
                    cek = True

        count = 0
        cek = True
        while cek:
            if HP_pemain1 == 0 and HP_pemain2 == 0:
                cek = False
                menang = "seri"
            elif HP_pemain1 <= 0:
                cek = False
                menang = "pemain 2"
            elif HP_pemain2 <=  0:
                cek = False
                menang = "pemain 2"

            HP_pemain2 = (HP_pemain2-ATK_point1)
            HP_pemain1 -= ATK_point2
            count += 1
        if menang == "pemain 2":
            print(f"Pemain 2 akan menang dalam {count-1} ronde.")
        if menang == "pemain 1":
            print(f"Pemain 1 akan menang dalam {count-1} ronde.")
        if menang == "seri":
            print("Permainan berakhir dengan seri.")



    if role_pemain2 == "archer":
        HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
        ATK_point2 = 5
        if HP_pemain2 > 150 or HP_pemain2 < 0:
            cek = False
            while (HP_pemain2 > 150 or HP_pemain2 < 0) and cek == False:
                print("HP tidak Valid!")
                HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
                if 0 <= HP_pemain2 <= 150:
                    cek = True

        count = 0
        cek = True
        while cek:
            if HP_pemain1 == 0 and HP_pemain2 == 0:
                cek = False
                menang = "seri"
            elif HP_pemain1 <= 0:
                cek = False
                menang = "pemain 2"
            elif HP_pemain2 <=  0:
                cek = False
                menang = "pemain 2"

            HP_pemain2 = (HP_pemain2-ATK_point1)
            HP_pemain1 -= ATK_point2
            count += 1
        if menang == "pemain 2":
            print(f"Pemain 2 akan menang dalam {count-1} ronde.")
        if menang == "pemain 1":
            print(f"Pemain 1 akan menang dalam {count-1} ronde.")
        if menang == "seri":
            print("Permainan berakhir dengan seri.")



    if role_pemain2 == "paladin":
        HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
        ATK_point2 = 5
        if HP_pemain2 > 100 or HP_pemain2 < 0:
            cek = False
            while (HP_pemain2 > 100 or HP_pemain2 < 0) and cek == False:
                print("HP tidak Valid!")
                HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
                if 0 <= HP_pemain2 <= 100:
                    cek = True

        count = 0
        cek = True
        while cek:
            if HP_pemain1 == 0 and HP_pemain2 == 0:
                cek = False
                menang = "seri"
            elif HP_pemain1 <= 0:
                cek = False
                menang = "pemain 2"
            elif HP_pemain2 <=  0:
                cek = False
                menang = "pemain 2"

            HP_pemain2 = (HP_pemain2-ATK_point1)*1.1
            HP_pemain1 -= ATK_point2
            count += 1
        if menang == "pemain 2":
            print(f"Pemain 2 akan menang dalam {count-1} ronde.")
        if menang == "pemain 1":
            print(f"Pemain 1 akan menang dalam {count-1} ronde.")
        if menang == "seri":
            print("Permainan berakhir dengan seri.")


if role_pemain1 == "archer":
    ATK_point1 = 5
    HP_pemain1 = float(input(f"Masukan sisa HP {role_pemain1} (P1): "))
    if HP_pemain1 > 150 or HP_pemain1 < 0:
        cek = False
        while (HP_pemain1 > 150 or HP_pemain1 < 0) and cek == False:
            print("HP tidak Valid!")
            HP_pemain1 = float(input(f"Masukan sisa HP {role_pemain1} (P1): "))
            if 0 <= HP_pemain1 <= 150:
                cek = True
    
    
    role_pemain2 = input("Masukkan role pemain 2: ")

    
    if role_pemain2 == "warrior":
        HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
        ATK_point2 = 10
        if HP_pemain2 > 100 or HP_pemain2 < 0:
            cek = False
            while (HP_pemain2> 100 or HP_pemain2 < 0) and cek == False:
                print("HP tidak Valid!")
                HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
                if 0 <= HP_pemain2 <= 100:
                    cek = True

        count = 0
        cek = True
        while cek:
            if HP_pemain1 == 0 and HP_pemain2 == 0:
                cek = False
                menang = "seri"
            elif HP_pemain1 <= 0:
                cek = False
                menang = "pemain 2"
            elif HP_pemain2 <=  0:
                cek = False
                menang = "pemain 2"

            HP_pemain2 = (HP_pemain2-ATK_point1)
            HP_pemain1 -= ATK_point2
            count += 1
        if menang == "pemain 2":
            print(f"Pemain 2 akan menang dalam {count-1} ronde.")
        if menang == "pemain 1":
            print(f"Pemain 1 akan menang dalam {count-1} ronde.")
        if menang == "seri":
            print("Permainan berakhir dengan seri.")



    if role_pemain2 == "archer":
        HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
        ATK_point2 = 5
        if HP_pemain2 > 150 or HP_pemain2 < 0:
            cek = False
            while (HP_pemain2 > 150 or HP_pemain2 < 0) and cek == False:
                print("HP tidak Valid!")
                HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
                if 0 <= HP_pemain2 <= 150:
                    cek = True

        count = 0
        cek = True
        while cek:
            if HP_pemain1 == 0 and HP_pemain2 == 0:
                cek = False
                menang = "seri"
            elif HP_pemain1 <= 0:
                cek = False
                menang = "pemain 2"
            elif HP_pemain2 <=  0:
                cek = False
                menang = "pemain 2"

            HP_pemain2 = (HP_pemain2-ATK_point1)
            HP_pemain1 -= ATK_point2
            count += 1
        if menang == "pemain 2":
            print(f"Pemain 2 akan menang dalam {count-1} ronde.")
        if menang == "pemain 1":
            print(f"Pemain 1 akan menang dalam {count-1} ronde.")
        if menang == "seri":
            print("Permainan berakhir dengan seri.")


    if role_pemain2 == "paladin":
        HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
        ATK_point2 = 5
        if HP_pemain2 > 100 or HP_pemain2 < 0:
            cek = False
            while (HP_pemain2 > 100 or HP_pemain2 < 0) and cek == False:
                print("HP tidak Valid!")
                HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
                if 0 <= HP_pemain2 <= 100:
                    cek = True
        count = 0
        cek = True
        while cek:
            if HP_pemain1 == 0 and HP_pemain2 == 0:
                cek = False
                menang = "seri"
            elif HP_pemain1 <= 0:
                cek = False
                menang = "pemain 2"
            elif HP_pemain2 <=  0:
                cek = False
                menang = "pemain 2"

            HP_pemain2 = (HP_pemain2-ATK_point1)*1.1
            HP_pemain1 -= ATK_point2
            count += 1
        if menang == "pemain 2":
            print(f"Pemain 2 akan menang dalam {count-1} ronde.")
        if menang == "pemain 1":
            print(f"Pemain 1 akan menang dalam {count-1} ronde.")
        if menang == "seri":
            print("Permainan berakhir dengan seri.")




    
if role_pemain1 == "paladin":
    ATK_point1 = 5
    HP_pemain1 = float(input(f"Masukan sisa HP {role_pemain1} (P1): "))
    if HP_pemain1 > 100 or HP_pemain1 < 0:
        cek = False
        while (HP_pemain1 > 100 or HP_pemain1 < 0) and cek == False:
            print("HP tidak Valid!")
            HP_pemain1 = float(input(f"Masukan sisa HP {role_pemain1} (P1): "))
            if 0 <= HP_pemain1 <= 100:
                cek = True
        

    role_pemain2 = input("Masukkan role pemain 2: ")
    if role_pemain2 == "warrior":
        HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
        ATK_point2 = 10
        if HP_pemain2 > 100 or HP_pemain2 < 0:
            cek = False
            while (HP_pemain2> 100 or HP_pemain2 < 0) and cek == False:
                print("HP tidak Valid!")
                HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
                if 0 <= HP_pemain2 <= 100:
                    cek = True

        count = 0
        cek = True
        while cek:
            if HP_pemain1 == 0 and HP_pemain2 == 0:
                cek = False
                menang = "seri"
            elif HP_pemain1 <= 0:
                cek = False
                menang = "pemain 2"
            elif HP_pemain2 <=  0:
                cek = False
                menang = "pemain 2"

            HP_pemain1 = (HP_pemain1-ATK_point2)*1.1
            HP_pemain2 -= ATK_point1
            count += 1
        if menang == "pemain 2":
            print(f"Pemain 2 akan menang dalam {count-1} ronde.")
        if menang == "pemain 1":
            print(f"Pemain 1 akan menang dalam {count-1} ronde.")
        if menang == "seri":
            print("Permainan berakhir dengan seri.")



    if role_pemain2 == "archer":
        HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
        ATK_point2 = 5
        if HP_pemain2 > 150 or HP_pemain2 < 0:
            cek = False
            while (HP_pemain2 > 150 or HP_pemain2 < 0) and cek == False:
                print("HP tidak Valid!")
                HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
                if 0 <= HP_pemain2 <= 150:
                    cek = True

        count = 0
        cek = True
        while cek:
            if HP_pemain1 == 0 and HP_pemain2 == 0:
                cek = False
                menang = "seri"
            elif HP_pemain1 <= 0:
                cek = False
                menang = "pemain 2"
            elif HP_pemain2 <=  0:
                cek = False
                menang = "pemain 2"

            HP_pemain1 = (HP_pemain1-ATK_point2)*1.1
            HP_pemain2 -= ATK_point1
            count += 1
        if menang == "pemain 2":
            print(f"Pemain 2 akan menang dalam {count-1} ronde.")
        if menang == "pemain 1":
            print(f"Pemain 1 akan menang dalam {count-1} ronde.")
        if menang == "seri":
            print("Permainan berakhir dengan seri.")



    if role_pemain2 == "paladin":
        HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
        ATK_point2 = 5
        if HP_pemain2 > 100 or HP_pemain2 < 0:
            cek = False
            while (HP_pemain2 > 100 or HP_pemain2 < 0) and cek == False:
                print("HP tidak Valid!")
                HP_pemain2 = float(input(f"Masukan sisa HP {role_pemain2} (P2): "))
                if 0 <= HP_pemain2 <= 100:
                    cek = True
        count = 0
        cek = True
        while cek:
            if HP_pemain1 == 0 and HP_pemain2 == 0:
                cek = False
                menang = "seri"
            elif HP_pemain1 <= 0:
                cek = False
                menang = "pemain 2"
            elif HP_pemain2 <=  0:
                cek = False
                menang = "pemain 2"

            HP_pemain1 = (HP_pemain1-ATK_point2)*1.1
            HP_pemain2 -= (HP_pemain2-ATK_point1)*1.1
            count += 1
        if menang == "pemain 2":
            print(f"Pemain 2 akan menang dalam {count-1} ronde.")
        if menang == "pemain 1":
            print(f"Pemain 1 akan menang dalam {count-1} ronde.")
        if menang == "seri":
            print("Permainan berakhir dengan seri.")
