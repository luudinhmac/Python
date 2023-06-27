def quicksort(m):

    if len(m) < 2:
        return m
    else:
        pivot = m[0]
        left = [i for i in m[1:] if i <= pivot]
        right = [i for i in m[1:] if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)


def insertsort(m):
    if len(m) < 2:
        return m
    for i in range(1, len(m)):
        select = m[i]
        post = i - 1
        while post >= 0 and m[post] > select:
            m[post+1] = m[post]
            post -= 1
        m[post+1] = select
    return m


def selectionsort(m):
    for i in range(0, len(m)-1):
        min_max = i
        for j in range(i+1, len(m)):
            if m[j] < m[min_max]:
                min_max = j
        m[i], m[min_max] = m[min_max], m[i]
    return m


def bublesort(m):
    for i in range(len(m)-1):
        for j in range(0, len(m)-1-i):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
    return m


def sequence_seach(m, x):
    idx = -1
    for i in range(len(m)):
        if m[i] == x:
            idx = i
        else:
            idx = -1
    return idx


def binary_search(m, x):
    mid = len(m)//2
    if m[mid] == x:
        return mid
    elif m[mid] < x:
        mid = mid + 1
    else:
        mid = mid - 1
    return mid


m = [6, 1, 3, 6, 3, 6, 9, 2, 10, 3]


# merge sort
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    half_left = arr[:mid]
    haft_right = arr[mid:]
    half_left = merge_sort(half_left)
    haft_right = merge_sort(haft_right)
    return merge(half_left, haft_right)

def merge(left, right):
    idx_lert = 0
    idx_right = 0
    n1 = len(left) # len left
    n2 = len(right)  # len right
    merged = []
    while idx_lert < n1 and idx_right < n2:
        if left[idx_lert] < right[idx_right]:
            merged.append(left[idx_lert])
            idx_lert += 1
        else:
            merged.append(right[idx_right])
            idx_right += 1
    while idx_lert < n1:
        merged.append(left[idx_lert])
        idx_lert+=1
    while idx_right < n2:
        merged.append(right[idx_right])
        idx_right+=1
    return merged

print(merge_sort(m))


