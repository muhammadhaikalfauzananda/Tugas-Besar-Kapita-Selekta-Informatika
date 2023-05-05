import os.path
import os
for x in range(10):
    x += 1
    file_path_txt = os.path.join(f'teks{x}.txt')
    file_path_lzw = os.path.join(f'teks{x}.lzw')
    size_txt = os.path.getsize(file_path_txt)
    size_lzw = os.path.getsize(file_path_lzw)
    print(f'Ukuran file teks{x} sebelum kompresi ', size_txt, 'bytes')
    print(f'Ukuran file teks{x} setelah kompresi ', size_lzw, 'bytes')
    persentase_pengurangan = (1 - (size_lzw/size_txt)) * 100
    print(f'presentase pengurangan file {x} ', persentase_pengurangan, 'bytes')
