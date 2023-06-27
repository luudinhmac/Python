"""
Hay viet chuong trinh su dung ky thuat list comprehension de in ra
man hinh cac so nguyen duong nho hon hoac bang n va chia het cho 7.
Voi n la mot so duoc nhap tu ban phim.
"""
# n = int(input())
# div7 = [i for i in range(1, n+1) if i <= n and i % 7 == 0]
# print(div7)

"""
Hay viet chuong trinh su dung ky thuat list comprehension de in ra man
hinh cac so nguyen duong nho hon hoac bang n ma co chua so 3 trong no.
Voi n la mot so duoc nhap tu ban phim.
"""
# n=int(input())
# three = [i for i in range(1,n+1) if '3' in list(str(i))]
# print(three)

# Hay viet chuong trinh su dung ky thuat list comprehension de in ra 
# man hinh cac so luong cac dau cach nam trong mot doan van ban
# duoc nhap vao tu ban phim.

string=input()
spaces = [ i for i in string if i == ' ' ]
print(len(spaces))

"""
Hay viet chuong trinh su dung ky thuat list comprehension de
 loai bo cac nguyen am: a,e,i,o,u ra khoi doan van ban
duoc nhap vao tu ban phim.
 Va in ra doan van ban sau khi da loai bo cac ky tu nay."""

 