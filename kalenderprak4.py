bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

hari = 0
i = 1

while i <= 12:
    if i == bulan:
        if i == 2:
            if tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0):
                hari = 29
            else:
                hari = 28
        elif i in [4, 6, 9, 11]:
            hari = 30
        else:
            hari = 31
    i += 1

print("Jumlah hari:", hari)