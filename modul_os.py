import os

# Informasi direktori
print("Folder saat ini ", os.getcwd())

# Informasi sistem
# nt Untuk windows, 'posix' untuk Unix/Linux/Mac
print("Sistem Oprasi ", os.name)

# Cek apakah file/direktori ada
print("File ada = ", os.path.exists("test.txt"))
print("Direktori ada = ", os.path.exists("Uji Folder"))

# Informasi file
if os.path.exists("test.txt"):
    print("Adalah file : ", os.path.isfile("test.txt"))
    print("Adalah direktori : ", os.path.isdir("Belajar-Python_modul"))
    print("Ukuran file : ", os.path.getsize("test.txt"))

# Path oprations

file_path = "D:\Coding\Belajar-Python-Modul/test.txt"
print("Direktori : ", os.path.dirname(file_path))
print("Nama file : ", os.path.basename(file_path))
print("Nama tanpa extension : ", os.path.splitext(file_path)[0])
print("Extension : ", os.path.splitext(file_path)[1])