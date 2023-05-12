import sys
from sys import argv
import struct
from struct import *

input_file = argv[1]
ukuran_tabel_maksimum = pow(2, 16)
file = open(input_file, "rb")
data_kompres = []
next_code = 256
data_dekompresi = ""
kalimat = ""

while True:
    rec = file.read(2)
    if len(rec) != 2:
        break
    (data, ) = unpack('>H', rec)
    data_kompres.append(data)

ukuran_kamus = 256
kamus = dict([(x, chr(x)) for x in range(ukuran_kamus)])

for kode in data_kompres:
    if not (kode in kamus):
        kamus[kode] = kalimat + (kalimat[0])
    data_dekompresi += kamus[kode]
    if not (len(kalimat) == 0):
        kamus[next_code] = kalimat + (kamus[kode][0])
        next_code += 1
    kalimat = kamus[kode]

out = input_file.split(".")[0]
output_file = open(out + "_decoded.txt", "w")
for data in data_dekompresi:
    output_file.write(data)

output_file.close()
file.close()
