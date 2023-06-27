def merge(left, right):
    merged = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx +=1
        else:
            merged.append(right[right_idx])
            right_idx +=1
    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx +=1
    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx +=1
    return merged

def merge_sort(arr):
    if len(arr) <=1:
        return  arr
    mid  = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


arr = [1,2,5,2,3,8,7]
merge_sort(arr)
print(merge_sort(arr))