def power(a, n):
    if n == 0:
        return 1
    s=a
    for i in range(1,n):
        s*=a
    return s

a = float(input())
n = int(input())
print(power(a,n))