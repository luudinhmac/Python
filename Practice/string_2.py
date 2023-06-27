"""
1. Viết ct kiểm tra tính hợp lệ của mật khẩu
- Mật khẩu hợp lệ khi có ít nhất 6 ký tự, chứa ít nhất 1 chữ cái, chứa ít nhất 1 chữ số


"""
passwords = "passworDd1"

digit = bool
alpha = bool
if len(passwords) <6:
    print("Mat khau khong hop le")
else:
    for i in passwords:
        if i.isalpha():
            alpha = True
        else: alpha = False
        if i.isdigit():
            digit =True
        else: digit = False
if digit ==True and alpha ==True:
    print("Mat khau hop le")
else:
    print("Mat khau khong hop le")
