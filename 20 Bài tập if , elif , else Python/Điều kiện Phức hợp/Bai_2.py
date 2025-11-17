nam = int(input("Nhập 1 năm : "))

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("năm nhuận")
else:
    print("không phải năm nhuận")