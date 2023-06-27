for i in range(10, 51):
    if i % 3 != 0:
        continue
    else:
        pass
        # print(i, end=" ")


# s= 1!+2!+...+10!
gt = 1
s = 0
for i in range(1, 11):
    gt = i*gt
    s += gt
print(f"Tong giai thua: {s}")

# so hoan chinh la 1 so nguyen duong ma tong cac uoc nguyen duong chinh thuc cua no bang chinh no. tim ta ca cac so hoan hao trong khoang tu 1 toi 1000


for i in range(1, 1001, 1):
    s = 0
    for j in range(1, i, 1):
        if i % j == 0:
            s = s + j
    if s == i:
        print(i, end=" ")
