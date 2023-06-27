# change arr 1d to 2d
import numpy as np
m = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,3]])
print(m)


def maxtrix_reverse(arr):
    n = np.zeros((m.shape[1],m.shape[0]))
    count = 0
    for row in arr:
        n[:,count] = row
        count += 1
    return n

print(maxtrix_reverse(m))
