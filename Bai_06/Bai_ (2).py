diem_so = [8.5, 7.0, 9.2, 5.8, 5.5, 8.8]

for diem in diem_so:
    if diem >= 8:
        loai = "GIỎI"
    elif 6.5 <= diem <= 7.9:
        loai = "Khá"
    else:
        loai = "Trung bình"
    print(diem ,"-", loai)