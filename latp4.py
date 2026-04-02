#Input
hari = int(input("Masukkan jumlah hari: "))

#Proses
tahun = hari // 365
sisa = hari % 365

bulan = sisa // 30
sisa_hari = sisa % 30

#Output
print(hari, "hari adalah", tahun, "tahun,", bulan, "bulan,", sisa_hari, "hari")