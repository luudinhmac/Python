# selection sort
# Select the smallest element in the original element
# Sau đó xem dãy hiện hành chỉ có n-1 phần tử của dãy ban đầu, bắt đầu từ vị trí thứ 2
# Lặp lại quá trình cho tới khi dãy còn 1 phần tử

# m = [3, 2, 5, 6, 4, 9, 8]
m = [4, 2, 1, 7, 9, 3, 6, 10]

def selection_sort(m):
    for i in range(len(m)-1):
        max_min = i
        for j in range(i+1, len(m)):
            if m[j] < m[max_min]:
                max_min = j
        m[max_min], m[i] = m[i], m[max_min]
    return m


selection_sort(m)
print(m)
