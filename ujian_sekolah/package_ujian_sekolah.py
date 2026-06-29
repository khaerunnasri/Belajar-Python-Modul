def ambil_soal(lokasi_file):
    soal_asli = []
    with open(lokasi_file, "r") as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli


def buat_soal(lokasi_file):

    soal_asli = ambil_soal(lokasi_file)

    import random
    # Acak soal
    random.shuffle(soal_asli)

    soal_ujian = []
    for i in range(10):
        soal = soal_asli[i] # pertanyaan|jawaban1,jawaban2, jawaban3,jawaban4
        data = soal.split("|") # ["pertanyaan","jawaban1, jawaban1,jawaban2,jawaban3,jawaban4"] ini sudah jadi list

        pertanyaan = data[0] # pertanyaan
        semua_jawaban = data[1] # "jawaban1,jawaban2,jawaban3,jawaban4" masih dalam bentuk str blm arry

        jawaban = semua_jawaban.split(",") # ["jawaban1, jawaban1,jawaban2,jawaban3,jawaban4"] sudah menjadi list atau arry
        jawaban_benar = jawaban[0] # "Jawaban1" benar

        # Acak jawaban
        random.shuffle(jawaban) # ["jawaban2", "jawaban1", "jawaban4", "jawaban3"] di acak jawaban 
        
        soal_ujian.append({
                "pertanyaan" : pertanyaan,
                "jawaban" : jawaban,
                "jawaban_benar" : jawaban_benar
        })

    return soal_ujian
