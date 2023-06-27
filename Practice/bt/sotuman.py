"""

"""
with open("SOTUMAN.INP") as f:
    a =f.readlines()
lst = []
for element in a[1].split():
    sum =0
    for number in element:
        sum+= int(number)**3
    if sum == int(element):
        lst.append(int(element))
print(lst)
lst.sort()
print(lst)

lst_out= ""
for x in lst:
    lst_out = lst_out + str(x) + " "

with open("SOTUMAN.OUT","w") as fo:
    fo.write(lst_out)
    