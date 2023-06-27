"""Viet ct chuyen tin nhan sang mat ma bang
a# = "abcdefghijklmnopqrstuvwxyz"
b# = "zxcvbnmasdfghjklqwertyuiop"
"""

mess = "hello world"
a = "abcdefghijklmnopqrstuvwxyz"
b = "zxcvbnmasdfghjklqwertyuiop"
s = ""
for i in mess:
    k = a.find(i)
    s =s + b[k]
print(s)
            