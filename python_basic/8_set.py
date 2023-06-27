# set chưa cac phan tu khong trung nhau
# set add va remove rat nhanh
# set sử dụng hash table
# Lấy phần dư chia 10 -> lưu vào ô tương ứng
# vd : 99/10 = 9 -> lưu vào ô số 9
# tìm kiếm: 99/10 =9 -> tìm vào ô số 9
ss = set((1, 2, 3))
print(type(ss))

s = {1, 2, 4, 5, 12, 5, 2}
s.add(2)
s.remove(12)
print(s)
s.clear()
print(s)
print(0 in s)

s1 = {1, 2, 3, 5, 3, 4}
s2 = {4, 5, 2, 7}
print(s1.union(s2))
print(s1.difference(s2))
print(s1.intersection(s2))

