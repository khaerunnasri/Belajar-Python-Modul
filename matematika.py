# Modul matematika

PI = 3.14159

NAMA_PEMBUAT = "Tim Matematika"


def tambah(a, b):
    """Menambah dua angka""" # ini adalah docstring atau dokumentasi untuk memberitahu pengguna cara penggunaan atau code untuk apa dll
    return a + b

def kurang(a, b):
    """Mengurangi dua angka"""
    return a - b

def kali(a, b):
    """
    Mengalikan dua angka
    """
    return a * b

def bagi(a, b):
    """
    Membagi dua angka
    """
    if b != 0:
        return a / b 
    else:
        return "Error : Bilangan tidak boleh 0"
    

if __name__ == "__main__": # pengecekan main Menjelaskan bahwa ini modul bukan file utama 
    print("Program ini tidak bisa dijalankan sebagai modul")
    