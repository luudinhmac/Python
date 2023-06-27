size = int(input())

for i in range(size+1):
  for j in range(size -i):
    print(end =' ')
  for j in range(i+1):
    print('*',end= ' ')
  print()

for i in range(size, 0, -1):
    for j in range(size - i +1, 0, -1):
        print(end=' ')
    for j in range(i):
        print('*', end=' ')
    print()
