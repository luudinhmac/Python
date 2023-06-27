my_tuple = tuple(input().split())
print(my_tuple)
if '30' not in my_tuple:
    print("NOT FOUND")
else:
    count = my_tuple.count('30')
    if count == 1:
        print(f"FOUND only one time at index: {my_tuple.index('30')}")
    else:
        print(f"The first occurrence is at index: {my_tuple.index('30')}")
        print(f"And the last occurrence is at index: {len(my_tuple) - 1 - my_tuple[::-1].index('30')}")
