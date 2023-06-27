# move zero to last list
import numpy as np

ar = [
    [1, 2, 3],
    [4, 5, 6],
    [8, 9, 10]]

arr = np.array(ar)
print(f"Mang tren la mang {arr.ndim} chieu")
print(f"Kich thuoc cua mang la {arr.shape}")
print(f"So phan tu cua mang la: {arr.size}")

L = [1, 2, 3, 4, 52, 4, 2, 4, 4]
x = np.array(L)
y = np.array(L).reshape(3, 3)
z = np.arange(0, 9, 1).reshape(3, 3)
z1 = np.linspace(1, 10, 4)
z2 = np.zeros((2, 2))
z3 = np.ones((2, 2))

print(x)
print(y)
print(f"Ve lai mang co gia tri tu 0 den 9, cach nhau 1 don vi, mang 3x3 \n{z}")
print(f"Tao mang co gia tri tu 1 toi 10 cach 4 doan bang nhau \n {z1}")
print(f"Tạo mảng toàn 0 có size là (2,2)\n {z2}")
print(f"Tạo mảng toàn 1 có size là (2,2)\n {z3}")

print(f"Dong 0 cot 1: {arr[0,1]}")
print(f"Dong 0: {arr[0,]}")
print(f"Xuat cot cuoi cung: {arr[ :, -1]}")
print(f"Xuat phan tu dong 1 den 2 nam trong cot 1 : {arr[1:3,1]}")

print("Tim kiem 17 có trong mảng hay không? ")
k=0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if (arr[i,j]==17):
            print(i,j)
            k = 1
        else: 
            k =0
if k ==0:
    print("Khong tim thay phan tu trong mang")          
