with open("SONGUYENTO.INP") as fr:
    a = fr.readline()
sums = sum([int(i) for i in a])  #list comprehension
def check_prime(n):
    if n < 2:
        return "NO"
    for i in range(2, n//2+1):
        if n % i == 0:
            return "NO"
    return "YES"

with open("SONGUYENTO.OUT","w") as fo:
    fo.write(str(sums)+"\n"+check_prime(sums))