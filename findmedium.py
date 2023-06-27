

# import math

# def merge_median(m1, m2):
#     m3 = m1 + m2
#     m3.sort()  # Sắp xếp mảng m3
#     n = len(m3)
#     if n % 2 == 1:
#         median = m3[(n - 1) // 2]
#     else:
#         median = (m3[n // 2] + m3[(n // 2) - 1]) / 2
#     return median


# def find_medium(sorted_arr1, sorted_arr2):
#     m,n = len(sorted_arr1), len(sorted_arr2)

#     if (m+n) ==0:
#         return
#     if m> n:
#         return find_medium(sorted_arr1, sorted_arr2)
#     left =0
#     right = m
#     while left <= right:
#         partleftarr1 = (left+ right) //2
#         partleftarr2 = (m+n)//2 -partleftarr1
#         maxLeft1 = math.inf if partleftarr1 ==0 else sorted_arr1[partleftarr1-1]
#         maxLeft2 = math.inf if partleftarr2 ==0 else sorted_arr2[partleftarr2-1]
#         minRinght1 = math.inf if partleftarr1 ==n else sorted_arr1[partleftarr1]
#         minRinght2 = math.inf if partleftarr2 ==n else sorted_arr2[partleftarr2]

#         if maxLeft1 <=minRinght2 and maxLeft2 <= minRinght1:
#             if (m+n)%2==1:
#                 return max(maxLeft1, maxLeft2)
#             return (max(maxLeft1,maxLeft2) + min(minRinght1,minRinght2))/2

#         elif maxLeft1 < minRinght1:
#             left = partleftarr1 +1
#         else:
#             right = partleftarr1-1


# m1 = [1,3,5,7,9,11]
# m2 = [2,4,6,8,10]

# def find_median(m1, m2):

#     n1 = len(m1)
#     n2 = len(m2)
#     if n1+n2 ==0:
#         return
#     merged = []

#     i = 0
#     j = 0
#     while i < n1 and j < n2:
#         if m1[i] <= m2[j]:
#             merged.append(m1[i])
#             i += 1
#         else:
#             merged.append(m2[j])
#             j += 1

#     while i < n1:
#         merged.append(m1[i])
#         i += 1

#     while j < n2:
#         merged.append(m2[j])
#         j += 1

#     n = len(merged)
#     if n % 2 == 1:
#         median = merged[(n - 1) // 2]
#     else:
#         median = (merged[n // 2] + merged[(n // 2) - 1]) / 2

#     return median

# print(find_median(m1,m2))

