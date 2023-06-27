str1 = "English = 78 Science = 83 Math = 85 History = 77"

st = str1.split()
sum= 0
count = 0
for i in st:
    if i.isdigit():
        sum+=int(i)
        count+=1
print(sum)
print(sum/count)
