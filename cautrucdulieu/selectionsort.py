m = [4, 2, 1, 7, 9, 3, 6, 10]


def selection_sort(m):
    for i in range(len(m)-1):
        m_m = i
        for j in range(i+1, len(m)):
            if m[j] < m[m_m]:
                m_m = j
        m[m_m], m[i] = m[m_m], m[i]

selection_sort(m)
print(m)
