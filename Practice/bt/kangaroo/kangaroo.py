with open("KANGAROO.INP") as fi:
    n,a,b = map(int,fi.readline().split())
for y in range(n//b,-1,-1):
    if (n-b*y)%a ==0:
        count_m = y+ (n-b*y)/a
        break
with open("KANGAROO.OUT", "w") as fo:
    fo.write(str(int(count_m)))