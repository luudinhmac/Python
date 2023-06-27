# "r", for reading
# "w", for writing
# "a", for appending
# "r+", for both reading and writing

# file = open("20/test.txt", "r+")
# #print(file.read())
# print(file.readline())
# print(file.readlines())
# print(list(file.readline()))
# print(file.write("Hello"))
# file.close()

# Tự động đóng file sau khi mở không cần dùng close
with open("20/test1.txt","r+") as file:
    print (file.read())

file = open("20/test1.txt")
print(file.read())