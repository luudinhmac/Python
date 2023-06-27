# r = 6
# for i in range(r+1):
#     for j in range(i):
#         print('*',end ='')
#     print()

# num = 4
# for i in range(num):
#     for j in range(num -i -1):
#         print(end = ' ')
#     for j in range(i +1):
#         print('*',end = ' ')
#     print()

# n = 6
# for row in range(n):
#     for col in range(n+1):
#         if (row == 0 and col%3!=0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
#             print('*',end ='')
#         else:
#             print(' ', end='')
#     print()


# size = int(input())

# for i in range(size, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print()

# size=int(input())
# for i in range(1, size+1):
#   for j in range(1,i+1):
#     print(i*j,end ='  ')
#   print()

# size = int(input())

# for i in range(size+1):
#   for j in range(size -i):
#     print(end =' ')
#   for j in range(i+1):
#     print('*',end= ' ')
#   print()

# for i in range(size, 0, -1):
#     for j in range(size - i +1, 0, -1):
#         print(end=' ')
#     for j in range(i):
#         print('*', end=' ')
#     print()


n = int(input())

count = n - 1

for i in range(1, n + 1):
    for j in range(2, i):
        if i % j == 0:
            count = count - 1
            break

print(count)
