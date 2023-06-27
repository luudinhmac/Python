m = [3, 4, 6, 8, 0, 1, 2]


def bublesort(m):
    for i in range(len(m)-1):
        for j in range(0, len(m)-1-i):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]


# bublesort(m)
# print(m)
def buble(m):
    for i in range(len(m)-1, -1, -1):
        for j in range(i):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]

buble(m)

print(m)