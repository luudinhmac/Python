# tim kiem tuan tu
m = [1, 2, 3, 4, 5, 6,7]


def sequence_search(m, x):
    idx = -1
    for i in range(len(m)):
        if x == m[i]:
            idx = i
    return idx


# print(sequence_search(m,2))

# tim kiem nhi phan dung de quy
def binary_search(m, left, right, x):
    mid = left + (right-left)//2
    if left <= right:
        if m[mid] == x:
            return mid
        if m[mid] > x:
            return binary_search(m, left, mid-1, x)
        return binary_search(m, mid+1, right, x)
    return -1


l = len(m)
# print(binary_search(m,0,l-1,4))


def binary_search2(m, x):
    left = 0
    right = len(m)-1
    while left <= right:
        mid = (left + right)//2
        print(mid)
        if m[mid] == x:
            return mid
        elif x < m[mid]:
            right = mid - 1
        else:
            left = mid + 1


print(binary_search2(m, 5))
