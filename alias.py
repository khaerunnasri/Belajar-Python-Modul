import matematika as aritmatika

def tambah(a, b): # namba tambah ini hanya function bukan import modul
    print("Fungsi tambah")
    return a + b


if __name__== "__main__":

    hasil1 = aritmatika.tambah(10, 5) # nama tambah disini adalah import tari modul matematika alias math
    hasil2 = aritmatika.kali(5, 5)

    print(f"Hasil dari 10 + 5 = {hasil1} ")
    print(f"Hasil dari 5 * 5 = {hasil2} ")

    print(f"Nilai PI = {aritmatika.PI}")
    print(f"Pembuat = {aritmatika.NAMA_PEMBUAT} ")