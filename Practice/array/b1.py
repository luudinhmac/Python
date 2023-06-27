# Viet ct tao 1 array 2d voi vien ngoai la so 1, ben trong toan bo la so 0
import numpy as np
a, b = [int(x) for x in input("Nhập số dòng và số cột cách nhau bằng khoảng trắng: ").split()]

ar = np.ones((a, b))
print(ar.shape)

ar[0, :] = 0
ar[:, 0] = 0
ar[-1, :] = 0
ar[:, -1] = 0
print(ar)
s = np.ones_like('*')
print(s)

l = []