import sys
from sys import argv
from struct import *

input_file = argv[1]
Ukuran_tabel_maksimum = pow(2, 24)
file = open(input_file)
data = file.read()

size_kamus = 256
kamus = {chr(i): i for i in range(size_kamus)}
kalimat = ""
data_kompres = []

for simbol in data:
    kalimat_tambah_simbol = kalimat + simbol
    if kalimat_tambah_simbol in kamus:
        kalimat = kalimat_tambah_simbol
    else:
        data_kompres.append(kamus[kalimat])
        if (len(kamus) <= Ukuran_tabel_maksimum):
            kamus[kalimat_tambah_simbol] = size_kamus
            size_kamus += 1
        kalimat = simbol

if kalimat in kamus:
    data_kompres.append(kamus[kalimat])

out = input_file.split(".")[0]
output_file = open(out + ".lzw", "wb")
for data in data_kompres:
    output_file.write(pack('>H', int(data)))

output_file.close()
file.close()
