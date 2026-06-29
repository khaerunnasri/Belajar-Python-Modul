import json

file = open("contoh.json", "r") # dibuka filenya
text = file.read() # dibaca filenya
file.close() # ditutup

print(text) # tampilkan datanya blm di konfersi ke tipe data python

# Konfersi text json ke tipe data yang ada di python menjadi tipe dictionry
murid = json.loads(text) # loads digunakan untuk mengambil dari tipe data json berubah(dikonfersi) menjadi tipe data yg ada di python(list/dictionri)
print(type(murid))
print(murid.get("nama"))
print(murid.get("umur"))
print(murid.get("nilai"))

# Konfesi tipe data dr python dictonary ke json
sekolah = {
    "nama" : "Universitas Nusantara",
    "alamat" : "NTB",
    "jurusan" : [
        "Teknik Informatika",
        "Sistem Informasi"
    ]
}

text_json = json.dumps(sekolah) # dumps mengubah(konfersi) tipe data dari python menjadi json
print(text_json) # data sudah menjadi json 

file = open("sekolah.json", "w") # simpan ke dalam file
file.write(text_json) # tulis ke dalam file
file.close() # tutup file
