n = int(input("Nhập số : "))
tong = 0
for i in range(1 , n + 1):
    tong = tong + i
    print(f"+ Thêm {i} -> tổng : {tong}")
print(f"Kết quả : 1 + 2 + ... + {n} = {tong}")