
m = [5, 1, 3, 5, 7, 2, 6, 1, 5, 8, 5, 22, 4, 6, 33]

def insert_sort(m):
    for i in range(len(m)):
        element = m[i]
        pos = i-1
        while pos >=0 and element < m[pos]:
            m[pos+1] = m[pos]
            pos-=1

        m[pos+1] = element

    return m

insert_sort(m)
print(m)

# Thuật toán tốt nhất khi mảng đã được sắp xếp, ví dụ hight score của game. người chơi mới được
# chèn vào sẽ có số điểm chèn vào mảng để sắp xép