# bubble sort
# example
# cho m = [2,4,1,3,6,8]
# sort  m increase
# compare 2 (i,i+1) if m[i]> m[i+1]  then swap(i,i+1)

m = [2, 1, 2,3, 4, 6, 8]
list_m = range(0, len(m)-1, 1)
# list_m = range(len(m)-1, -1, -1)

def bublesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        print(i)
        for j in range(0, i, 1):
            if (arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # tmp = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = tmp
    # return arr


# k = bubble_sort(m)
l = bublesort(m)
for i in range(len(m)):
    print(m[i], end=' ')
