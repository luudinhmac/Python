# read data from file
with open("DAYXN.INP")as fi:
    x,n = map(int,fi.readline().split())
print(x,n)
def f(x):
    return sum([int(i)**2 for i in str(x)])
with open("DAYOUT.OUT","w") as fo:
    for k in range(n):
        fo.write(str(x)+" ")
        x = f(x)
