#Input jumlah hari
x = int(input("Masukkan lama proyek (hari): "))

#Proses konversi
tahun = x // 365
sisa_hari = x % 365
bulan = sisa_hari // 30
hari = sisa_hari % 30

#Output hasil konversi
print("=== HASIL KONVERSI ===")
print(f"{x} hari = {tahun} tahun, {bulan} bulan, {hari} hari")