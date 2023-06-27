# while

size = int(input())

i = size
while i >= 1:
    print(" " * (size - i), end="")
    j = i
    while j >= 1:
        print("*", end=" ")
        j -= 1
    print()
    i -= 1

i = 1
while i <= size:
    print(" "*(size - i), end="")
    j = 0
    while j < i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
