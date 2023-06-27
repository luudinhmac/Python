"""
Trong gio sinh hoat tap the 9a, co n hoc sinh(n<=45) xep hang doc. Moi hoc sinh co chieu cao a[i]. Hay viet ct dem so ban co chieu cao bang nhau nhieu nhat
Du lieu vao tu file XEPHANG.INP
- dong thu  nhat chua stn n
- dong thu 2 gom n so tu nhien a[i], moi so tuong ung voi chieu cao cua cac ban, cac so cach nhau 1 khoang trang
kq xuat ra file XEPHANG.OUT
gom 2 stn. so thu nhat ghi so ban co chieu cao tuong ung, so thu 2 ghi chieu cao
moi so cach nhau 1 khoang trang
"""
with open("XEPHANG.INP") as fr:
    a =fr.readline()
    lst = list(map(int,fr.readline().split()))
# lst_count = []
# for i in range(len(lst)):
#     t = lst.count(lst[i])
#     lst_count.append(t)
# lst_out =str(max(lst_count))+" "+str(lst[lst_count.index(max(lst_count))])
# with open("XEPHANG.OUT", "w") as fo:
#     fo.write(lst_out)


#c2
lst_out = []
eq = max(lst, key = lst.count)
print(eq)
count = lst.count(eq)
print(count)
lst_out.append(count, eq)