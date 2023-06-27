# n! = n*(n-1)!..1 
# fibonacci
# F1 =1 , F2 =2 , Fn = F(n-1) + F(n-2)
def tinh_giai_thua(n):
    if n==0:
        return 1
    else:
        return n*tinh_giai_thua(n-1)
print(tinh_giai_thua(8))