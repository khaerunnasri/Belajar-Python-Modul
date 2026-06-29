# APLIKASI KALKULATOR SEDERHANA

def app_penjumlahan():
    print("Oprasi Penjumlahan")
    try:
        angka1 = int(input("Masukkan angka1 : "))
        angka2 = int(input("Masukkan angka2 : "))
        hasil = angka1 + angka2
        print("Hasil Penjumlahan : ",hasil)
    except ValueError:
        print("Angka yang anda masukkan salah")
    print("=== PROGRAM SELESAI ===")
    input("Enter Untuk Lanjut")

def app_pengurangan():
    print("Oprasi Pengurangan")
    try:
        angka1 = int(input("Masukkan angka1 : "))
        angka2 = int(input("Masukkan angka2 : "))
        hasil = angka1 - angka2
        print("Hasil Pengurangan : ",hasil)
    except ValueError:
        print("Angka yang anda masukkan salah")

    print("=== PROGRAM SELESAI ===")
    input("Enter Untuk Lanjut")

def app_perkalian():
    print("Oprasi Perkalian")
    try:
        angka1 = int(input("Masukkan angka1 : "))
        angka2 = int(input("Masukkan angka2 : "))
        hasil = angka1 * angka2
        print("Hasil Perkalian : ",hasil)
    except ValueError:
        print("Angka yang anda masukkan salah")

    print("=== PROGRAM SELESAI ===")
    input("Enter Untuk Lanjut")

def app_pembagian():
    print("Oprasi Pembagian")
    try:
        angka1 = int(input("Masukkan angka1 : "))
        angka2 = int(input("Masukkan angka2 : "))
        hasil = angka1 / angka2
        print("Hasil Pembagian : ", hasil)
    except ValueError:
        print("Angka yang anda masukkan salah")

    print("=== PROGRAM SELESAI ===")
    input("Enter Untuk Lanjut")