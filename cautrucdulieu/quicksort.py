
m = [3, 2, 1, 5, 4, 2, 3]

def quicksort(m):
    if len(m) <2:
        return m
    else:
        pivot =m[0]
        left = [i for i in m[1:] if i <= pivot]
        right = [i for i in m[1:] if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    


def insert_sort(m):
    for i in range(len(m)):
        cursor = m[i]
        postion  = i-1
        while postion >=0 and m[postion] > cursor:
            m[postion+1] = m[postion]
            postion -=1
        m[postion+1] = cursor


def selectionsort(m):
    for i in range(len(m)-1):
        min = i
        for j in range(i+1,len(m)):
            if m[j] < m[min]:
                min = j
        m[i],m[min] = m[min],m[i]
    return m

selectionsort(m)
print(m)

