# tao 1 array bang numpy 8x8
# hang so 1 toi hang so 7 co gia [0 1 0 1 0 1 0 1]
# rieng hang so 8 : [1 0 1 0 1 0 1 0]

# Tao ma tran toan bo bang so 1
import numpy as np

arr = np.ones((8, 8))

for i in range(arr.shape[1]):
    if i % 2 != 0:
        arr[7, i] = 0
    else:
        arr[0:7, i] = 0
print(arr)
