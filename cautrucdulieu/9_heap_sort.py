# Heap sort
# 1. Goc co dia chi tai 0: co la tai dia chi 1 va 2

# 2. Gốc tại địa chỉ tại 1: có 2 lá tại địa chỉ 3 và 4
# 3. Gốc tại địa chỉ 2 : có lá tại địa chỉ 5
# 4. Gốc i có lá bên left 2*i+1 và lá right 2*i+2
# 5. List có n phần tử , thì gốc lớn max là (n//2-1)

def vun_goc(arr, root, length):
    l = 2*root+1
    r = 2*root+2
    if (2*root+1 == length):  # 3 check root have one child
        if (arr[l] > arr[root]):  # compare child in the left with root
            # if child > root => swap
            arr[l],arr[root] = arr[root],arr[l]
    else:  # root has 2 children
        if arr[l] > arr[r]:  # compare children left and child right
            temp = l  # if child_left > child_right =>  save largest value to variable temp
        else:  # child_left < child_right
            temp = r  # save largest value to variable temp

        if arr[root] < arr[temp]:  # Compare values of root with values of list at temp
            # if values root < values temp => swap
            arr[root], arr[temp] = arr[temp], arr[root]
           


def vun_cay(arr):
    l = len(arr) - 1  # lenth list approved

    r = len(arr)//2 - 1  # root index max in list

    while l >= 0:
        for j in range(r, -1, -1):  # scan all root in list, revert list
            vun_goc(arr, j, l)
    # max values in head list, => swap to end list approved
        
        arr[0], arr[l] = arr[l], arr[0]
        l -= 1  # reduce lethth 1 values to skip max values end list
        r = (l+1)//2 - 1  # increase 1 to next root


m = [4, 2, 1, 88, 12, 7]
vun_cay(m)
print(m)

# def heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     l = 2 * i + 1  # left = 2*i + 1
#     r = 2 * i + 2  # right = 2*i + 2

#  # See if left child of root exists and is
#  # greater than root

#     if l < n and arr[i] < arr[l]:
#         largest = l
#  # See if right child of root exists and is
#  # greater than root
#     if r < n and arr[largest] < arr[r]:
#         largest = r
#  # Change root, if needed
#     if largest != i:
#         (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
#   # Heapify the root.
#         heapify(arr, n, largest)

# # The main function to sort an array of given size

# def heapSort(arr):
#     n = len(arr)

#  # Build a maxheap.
#  # Since last parent will be at ((n//2)-1) we can start at that location.

#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)

#  # One by one extract elements

#     for i in range(n - 1, 0, -1):
#         (arr[i], arr[0]) = (arr[0], arr[i])  # swap
#         heapify(arr, i, 0)

# import heapq
# def heap_sort(arr):
#     heapq.heapify(arr)
#     result = []
#     while arr:
#         result.append(heapq.heappop(arr))
#     return result


# # Driver Code
# arr = [3, 5, 19, 22, 28, 100, 88, 77]
# print("Input Array: ", arr)
# print("Sorted Array: ", heap_sort(arr))
