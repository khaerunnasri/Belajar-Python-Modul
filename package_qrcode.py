import qrcode

# Membuat qr code
img = qrcode.make("Khaerun Nasri")

# Menyimpan qr code
img.save("qr_nasri.png")