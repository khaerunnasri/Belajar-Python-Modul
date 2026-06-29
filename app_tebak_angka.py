from app_tebak_angka import tebakan_angka

if __name__=="__main__":
    while True:
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")
        print("1. Tebak Angka")
        print("2. exit")
        print("=== PROGRAM TABAK ANGKA SEDERHANA ===")

        try:
            pilihan = int(input("Pilihan Menu : "))

            if pilihan == 1:
                tebakan_angka.tebak_angka()
            elif pilihan == 2:
                print("Exit")
                break
            else:
                print("Error, Pilihan tidak valid")
        except ValueError:
            print("Masukkan Angka")
        
