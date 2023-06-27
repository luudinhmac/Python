a=int(input())
b=int(input())
uc =0
for i in range(1,a):
    if a%i == 0 and b%i == 0:
        uc = i
print(uc)