# insertion sort

# example
# m =
# increase in ascending oder
#
# List has n element at address 0 has list sorted
# Get 1 adjacent element after subsequence find a way to insert into the subsequence before it is appropriate
# Repeat this insert from 2nd to last element

m = [6, 5, 3, 1, 8, 7, 2, 4]


def insert_sort(arr):
    n = len(arr)
    # if n <= 1:
    # return
    for i in range(n):
        key = arr[i]  # select 1 element assign to key
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# insert_sort(m)
# print(m)


