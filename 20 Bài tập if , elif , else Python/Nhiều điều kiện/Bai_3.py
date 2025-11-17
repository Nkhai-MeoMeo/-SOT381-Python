so = int(input("Nhập số điểm mà bạn cần kiểm tra : "))

if so >= 8.0:
    print("Giỏi")
elif so >= 6.5:
    print("Khá")
elif so >= 5.0:
    print("Trung bình")
elif so < 5.0:
    print("Yếu")