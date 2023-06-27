"""
Hay viet chuong trinh Python cho phep nhan mot so nguyen duong n>0 
tu ban phim va in ra gia tri tong binh phuong cua tat ca cac so le nho hon hoac bang n
"""
n = int(input())
sum =0
for i in range(n+1):
    if i%2 !=0:
        sum +=i**2
print(sum)