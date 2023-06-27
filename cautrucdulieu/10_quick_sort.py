# Quicksort
# Phan nhom phan tu tren danh sach dua vao tu khoa
# 1. Select key k=m[0]
# 2. Duyệt qua các phần tử và so sánh với phần tử khóa k và phân thành 2 nhóm

# select pivot = first element
## using list comprehension
def quick_sort(m):
    if len(m) < 2:
        return m
    else:
        pivot = m[0]
        Left = [i for i in m[1:] if i <= pivot]
        Right = [i for i in m[1:] if i > pivot]
        return quick_sort(Left) + [pivot] + quick_sort(Right)

## using for loops
def quick_sort_2(m):
    if len(m)<2:
        return m
    else:
        Left = []
        Right = []
        pivot = m[0]
        for i in m[1:]:
            if i <= pivot:
                Left.append(i)
            if i> pivot:
                Right.append(i)
        return quick_sort_2(Left) + [pivot] + quick_sort_2(Right)


# select pivot at last element

def quick_sort_last(m):
    if m<2:
        return m
    else:
        pivot = m[-1]
        Left = [x for x in m[:-1] if x <= pivot]
        Right = [x for x in m[:-1 ] if x > pivot]
    return quick_sort_last(Left) + [pivot] + quick_sort_last(Right)

# 

m = [8, 3, 1, 1,5, 9, 7, 4]
# qs = quick_sort_2(m)
# print(qs)

