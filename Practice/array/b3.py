# Tim gia tri max va gia tri min trong 2d array :
# ([[34,43,73],[82,22,12],[53,94,66]])
# Xuat ra vi tri index cua gia tri max va min do

import numpy as np

arr = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

max= min = arr[0, 0]
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i, j] > max:
            max = arr[i, j]           
        if arr[i, j] < min:
            min = arr[i, j]

print(max, min)
for a in range(arr.shape[0]):
    for b in range(arr.shape[1]):
        if max == arr[a,b]:
            print (a, b)
        if min == arr[a,b]:
            print(a,b)
