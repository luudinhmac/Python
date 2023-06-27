# List
list_test = [1,2,3,'helo']
print(len(list_test))
list_test.extend([3,2,55])

x = list_test[:]
list_test[3] = "python"
print(list_test)
print(x)

# Tuples
tuple_test = (1,2,3)
