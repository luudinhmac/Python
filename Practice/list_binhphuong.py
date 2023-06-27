n = int(input("Nhap so pt: "))
l = []
count = 0
while count <n:
    pt = int(input("Nhap vao phan tu: "))
    l.append(pt)
    count += 1
l2=[]
for i in l:
    l2.append(i*i)
print(l2)
count2 =0
for i in l2:
    if i > 50:
        count2 +=1

print(count2)