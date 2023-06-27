with open("UCLN.INP") as fi:
    m,n = map(int,fi.readline().split())

def UCLN(m,n):
    while m!=n:
        if m>n:
            m-=n
        else:
            n-=m
        return m
with open("UCLN.OUT","w")as fo:
    fo.write(str(UCLN(m,n)))