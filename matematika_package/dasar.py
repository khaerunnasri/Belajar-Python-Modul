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