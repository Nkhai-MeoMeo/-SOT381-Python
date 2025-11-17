chu = input("Nhập 1 ký tự để kiểm tra : ")

ki_tu = "a, e, i, o, u"

if len(chu) != 1:
    print("Vui lòng nhập 1 ký tự : ")
else:
    ch_lower = chu.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']

    if ch_lower in vowels:
        print("Nguyên âm")
    else:
        print("không nguyên âm")