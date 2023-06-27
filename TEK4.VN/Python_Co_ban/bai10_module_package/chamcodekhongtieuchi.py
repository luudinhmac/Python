# Viet chuong trinh tim tat ca cac so chia het cho 7 nhung khong phai boi so cua 5,
#  nam trong doan 2000 va 3200 (tinh ca 2000 va 3200). Cac so thu duoc se duoc
# in thanh chuoi tren mot dong, cach nhau bang dau phay.

j=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print (','.join(j))