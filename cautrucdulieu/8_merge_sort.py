# Merge sort
# Condition: 2 list was sorted
m1 = [1, 3, 5, 7, 10,12]
m2 = [2, 4, 6, 8, 9, 11]


def merge_sort(m1, m2):
    ms = [] # Init list null
    while m1 != [] and m2 != []:
        if m1[0] < m2[0]:
            ms.append(m1[0])
            m1 = m1[1:]
        else:
            ms.append(m2[0])
            m2 = m2[1:]
    # append last element to the list
    if m1 != []:
        ms = ms + m1
    if m2 != []:
        ms = ms + m2
    return ms


x = merge_sort(m1, m2)
print(x)
