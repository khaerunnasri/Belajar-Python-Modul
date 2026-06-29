import datetime

# Tanggal dan Waktu lengkap
sekarang = datetime.datetime.now()
print("Sekarang ",sekarang)

# Hari ini
hari_ini = datetime.date.today()
print("Hari ini", hari_ini)

# Hanya Waktu
waktu_sekarang = datetime.datetime.now().time()
print("Waktu Sekarang", waktu_sekarang)

# Membuat Tanggal tertentu
ulang_tahun = datetime.date(2022, 4, 22)
print("Ulang Tahun", ulang_tahun)

# Membuat waktu tertentu lengkap
acara = datetime.datetime(2025, 1, 10, 7, 30, 1)
print("Acara", acara)

print("Format Panjang", sekarang.strftime("%A, %d, %B, %Y"))
