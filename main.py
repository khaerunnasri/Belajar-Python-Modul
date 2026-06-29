import matematika

if __name__ == "__main__": # pengecekan main Biasanya aprogram utama adakn ada if __name__ == "__main__"

    hasil1 = matematika.tambah(10, 5)
    hasil2 = matematika.kali(5, 5)

    print(f"Hasil dari 10 + 5 = {hasil1} ")
    print(f"Hasil dari 5 * 5 = {hasil2} ")

    print(f"Nilai PI = {matematika.PI}")
    print(f"Pembuat = {matematika.NAMA_PEMBUAT} ")