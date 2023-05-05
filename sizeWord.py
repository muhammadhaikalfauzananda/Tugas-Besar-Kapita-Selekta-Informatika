from sys import argv
for i in range(10):
    i += 1
    input_file = f"teks{i}.txt"
    file = open(input_file)
    data = file.read()
    res = sum(not chr.isspace() for chr in data)
    print(f"jumlah karakter dalam file teks {i} : " + str(res))
