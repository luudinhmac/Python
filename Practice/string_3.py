"""
2. Cho người dùng đăng nhập vào mật khẩu để login / so sánh, nếu đúng mở cửa, nếu sai khoá đăng nhập thoát ct
"""

passwd = "password123"
pw = input("Enter password: ")

# while True:
#     if pw == passwd:
#         print("login successful")
#         break
#     else:
#         print("login failed")
#         print(count)
#         pw = input("ReEnter password: ")
#         count +=1
#     if count ==4:
#         exit()
count =1
while count <5:
    if pw == passwd:
        print("login successful")
        break
    else:
        print("login failed")
        count +=1
        pw = input("ReEnter Password")
