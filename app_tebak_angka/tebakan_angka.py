import random       

def tebak_angka():
    angka_acak = random.randint(1, 10)
    maksimal_tebakan = 3
    tebakan = 0

    while tebakan < maksimal_tebakan:
        tebakan +=1
        try:
            angka_user = int(input("Masukkan angka : "))
            if angka_user > angka_acak:
                print("Angka terlalu besar")
            elif angka_user < angka_acak:
                print("Angka terlalu kecil")
            else:
                print("Selamat Angka benar")
                break
        except ValueError:
            print("Anda harus input angka")
    else:
        print("Kamu telah melewati maksimal tebakan")
        print("Angka Acak adalah", angka_acak)
        
    input("enter untuk lanjut")