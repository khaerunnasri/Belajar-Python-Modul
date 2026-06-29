from calculator import operasi

if __name__== "__main__":
    while True:
        print("=== PROGRAM KALKULATOR SEDERHANA ===")
        print("1. Penjumlahan ")
        print("2. Pengurangan ")
        print("3. Perkalian ")
        print("4. Pembagian ")
        print("5. exit ")
        print("=== PROGRAM KALKULATOR SEDERHANA ===")

        try:
            pilihan = int(input("Masukkan Pilihan 1-5 : "))
            if pilihan == 1:
                operasi.app_penjumlahan()
            elif pilihan == 2:
                operasi.app_pengurangan()
            elif pilihan == 3:
                operasi.app_perkalian()
            elif pilihan == 4:
                operasi.app_pembagian()
            elif pilihan == 5:
                print("Sampai jumpa lagi (exit)")
                break
        except ValueError:
            print("Pilihan Yang anda masukkan tidak tersedia")
        finally: # Akan selalu dijalankan walau terjadi error atau tidak
            print("Keluar dan Selesai")


