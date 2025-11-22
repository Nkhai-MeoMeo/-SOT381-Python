tien_goc = 100_000_000
lai_suat = 0.07

nam = int(input("Nhập số năm cần đầu tư : "))
so_tien = tien_goc
for i in range(1 , nam + 1):
    so_tien += so_tien * lai_suat
print(f"{so_tien : }")