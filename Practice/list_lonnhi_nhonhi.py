import math
m = [1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 9]
nl = []
for i in m:
    if i == max(m):
        continue
    else:
        nl.append(i)
print("So lon nhi la: ", max(nl))
print(nl)
l_index = []
for j in range(len(m)):
    if m[j] == max(nl):
        l_index.append(j)
print(l_index)
