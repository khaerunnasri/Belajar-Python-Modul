from ujian_sekolah import package_ujian_sekolah

if __name__=="__main__":
    soal_ujian = package_ujian_sekolah.buat_soal("bank_soal.txt")
    opsi = ["A", "B", "C", "D"]

    jawaban_benar = 0
    jawaban_salah = 0

    for i in range(len(soal_ujian)):
        soal = soal_ujian[i]
        print("Pertanyaan ",i + 1, ":", soal["pertanyaan"])
        print("jawaban:")
        
        for j in range(len(soal["jawaban"])):
            jawaban = soal["jawaban"][j]
            print(opsi[j],".", jawaban)

        jawaban_user = input("Pilih jawaban (A/B/C/D) : ").upper()
        jawaban_user_index = opsi.index(jawaban_user)
        jawaban_asli_user = soal["jawaban"][jawaban_user_index]

        if jawaban_asli_user == soal["jawaban_benar"]:
            print("jawaban benar")
            jawaban_benar += 1
        else:
            print("jawaban salah")
            jawaban_salah +=1    

        print("Hasil Ujian")
        print("Jawaban benar: ", jawaban_benar)
        print("Jawaban salah: ", jawaban_salah)
        print("Hasil Ujian: ", jawaban_benar / (jawaban_benar+jawaban_salah) * 100, "%")
