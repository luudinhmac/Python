# Cho arr 2d: ([[34,43,73],[82,22,12],[53,94,66]])
# 1 sap xep de duoc nhu sau(doi cot dau voi cot cuoi)
# 2 doi vi tri hang dau cho hang 2
import numpy as np

L = [[34, 43, 73], [82, 22, 12], [53, 94, 66]]
ar = np.array(L)
print(f"Mang ban dau: {ar}")
# ar_ch = tuple(ar[:,0])  #de gia tri khong bi thay doi
# # neu k dung tuple th khi thay doi ar[:,-2] cung thay doi theo
# print(ar_ch)
# ar[:,0] = ar[:,2]
# print(ar)
# ar[:,2] = ar_ch
# print(f"1# {ar}")


#2
ar_ch2 = tuple(ar[0])
print(ar_ch2)
ar[0] = ar[1]
ar[1]= ar_ch2
print(ar)