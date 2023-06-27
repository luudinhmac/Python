#s = 1 + 1/(2^2)+...+ 1/(n^2)
# Du lieu vao tu file TONG.INP
#Dong dau tien ghi so tu nhien n
# Du lieu ra tu file TONG.OUT
# Dung dau "," de ngan cach phan nguyen va phan thap phan, lam tron 3 so thap phan

def tong(n):
    t = 0
    for i in range(1,n+1):
        t +=1/(i**2) 
    return t

with open("TONG.INP", "r") as f:
    n = int(f.read())
with open("TONG.OUT", "w") as fo:
    fo.write(str(round(tong(n),3)))