'''
Hay viet chuong trinh Python tim cac uoc nguyen duong cua mot so nguyen duong n>0 nhap tu ban phim.
Dinh dang dau vao: so n>0 nhap tu ban phim.
'''
L = []
n = int(input())
for i in range(1,n+1):
    if n%i ==0:
        L.append(i)

print(f"{n} have {len(L)} divisors")
for j in L:
    print(j,end =' ')
print('!')

# print(f"They are: {st}!")