n = int(input("Nhập số : "))
tong_le = 0
print(f"các số lẽ từ 1 đến {n}")

for i in range(1 , n + 1 , 2):
    tong_le = tong_le + 1
    print(f"+ {i}")
print(f"Kết quả : {tong_le}")