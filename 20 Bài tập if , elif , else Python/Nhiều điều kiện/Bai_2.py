a = int(input("Nhập số liệu của bạn : "))
b = int(input("Nhập số liệu của bạn : "))
c = int(input("Nhập số liệu của bạn : "))

lon_nhat = a 
if c > lon_nhat:
    lon_nhat = c
if b > lon_nhat:
    lon_nhat = b 
print("Số lớn nhất trong cả 3 số mà bạn đã đưa ra : ", lon_nhat)