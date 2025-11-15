chuoi = input("Nhập chuỗi cần kiểm tra : ")
co_python = "Python" in chuoi
co_programming = "Programming" in chuoi
if co_python and co_programming:
    print("chuỗi có chứa cả 'Python' và 'Programming'")
else:
    print("chuỗi không chứa đầy đủ cả 2 từ")