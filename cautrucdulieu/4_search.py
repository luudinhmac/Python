# sequential search Tìm kiếm tuần tự
# binary search: Tìm kiếm nhị phân


# Bài toán m = [1,2,4,5,7,9,11,13,15,18,19,22,28,35,53,123,129]
# Tìm kiếm số x = 13 có trong mảng m không, cho biết vị trí của nó.

# Sequential search:
# Duyệt qua tất cả các phần tử trong mảng để tìm kiếm

# binary search:
# lấy số cần tìm x=13 so sánh với phần tử trung tâm của mảng, để xác định x đang nằm ở khoản nào của mảng
# ý nghĩa thu hẹp phạm vi tìm kiếm

# Sequential
import time
m = [1, 2, 4, 5, 7, 9, 11, 13, 15, 18, 19, 22, 28, 35, 53, 123, 129]


def sequential_search(x, lists):
    index = -1
    for i in range(0, len(lists), 1):
        if lists[i] == x:
            index = i

    return index


t1 = time.time()
print(f"Sequential search: {sequential_search(123,m)}")
t2 = time.time()
print((t2-t1)*1000,  "ms")

# Binary search


def binary_search(lists, x):
    index_left = 0
    index_right = len(lists) - 1
    while index_left <= index_right:
        central = (index_left+index_right)//2
        if lists[central] == x:
            return central
        elif x < lists[central]:
            index_right = central - 1
        else:
            index_left = central + 1


t3 = time.time()
print(f"Binary search: {binary_search(m,123)}")
t4 = time.time()
print((t4-t3)*1000,  "ms")
