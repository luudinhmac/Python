"""
Viet ct su dung dict chua 10 username va password.
Chuong trinh yeu cau nhap username va password
neu username khong dung bao user khong ton tai
neu user dung ma password sai: bao sai mk
neu dung bao login thanh cong
"""

dic = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',
       'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j'}


user = input("Enter username: ")
passwd = input("Enter password: ")
while True:
    if user not in dic:
        print("User not found")
        user = input("ReEnter username: ")
    else:
        if passwd not in dic:
            print("Passwd not match")
            passwd = input("Enter password: ")
        else:
            print("Login successful")
            break
