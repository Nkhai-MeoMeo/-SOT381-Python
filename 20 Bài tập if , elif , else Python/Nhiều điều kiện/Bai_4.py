can_nang = float(input("Nhập số cận nặng của bạn (kg) : "))
chieu_cao = float(input("Nhập chiều cao của bạn (m) : "))

BMI = can_nang/(chieu_cao ** 2)
print("Chỉ số : ", round(BMI, 2))

if BMI < 18.5:
    print("Gầy")
elif BMI < 25:
    print("Bình thường")
else:
    print("Thừa cân")