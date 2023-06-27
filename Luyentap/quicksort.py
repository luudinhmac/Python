def swap(a,b):
    return b,a

def quick_sort(left,right):
    if left >= right:
        return
    i = left
    j = right
    