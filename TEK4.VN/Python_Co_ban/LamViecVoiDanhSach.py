'''
Trong cac bai tap tren, ban da lam quen voi cach su dung vong lap for. Bay gio chung ta se thu ket hop no de lam viec voi kieu du lieu danh sach voi bai tap duoi day.

Bai toan

Cho dau vao la mot danh sach rong (list = []). Hay viet chuong trinh cho phep xu ly cac thao tac va cap nhat vao danh sach nay nhu sau.

Dau tien chuong trinh nhan vao mot so nguyen duong n, tuong ung voi n thao tac xu ly tren danh sach. Sau do, user se nhap vao lan luot n thao tac tu ban phim voi moi dong tuong ung voi mot thao tac can thuc hien. Cu phap cua moi thao tac tuong ung nhu sau:

insert(i, e): Chen so nguyen e vao vi tri i.
print(): In ra danh sach.
remove(e): Xoa lan xuat hien dau tien cua so nguyen e.
append(e): Chen so nguyen e vao cuoi danh sach.
sort(): Sap xep danh sach.
pop(): Lay ra phan tu cuoi cung tu danh sach va xoa no khoi danh sach.
reverse(): Dao nguoc danh sach.
Chuong trinh can viet se duyet qua tung lenh theo thu tu n dong dau vao va thuc hien cac thao tac tuong ung tren danh sach list.

Dinh dang dau vao

Dong dau tien chua mot so nguyen duong n, bieu thi so luong cau lenh can thao tac tren danh sach. Moi dong i tiep theo se tuong ung voi mot lenh hay thao tac can thuc hien voi danh sach list trong so n cau lenh can thao tac. Cac dong nay chua cac cau lenh theo dung cu phap cua mot trong cac lenh duoc mo ta o tren.

Dieu kien

Cac phan tu duoc them vao danh sach phai la so nguyen.

Dinh dang dau ra

Khi gap cau lenh print se in ra man hinh danh sach list dang ton tai tai thoi diem do.

Vi du

9
append 1
append 2
append 3
insert 3 1
print
insert 4 3
pop
sort
print
append 1: Them 1 vao danh sach, list = [1].
append 2: Them 2 vao danh sach, list = [1,2].
append 3: Them 3 vao danh sach, list = [1,2,3].
insert 3 1: Chen gia tri 1 tai vi tri so 3, list = [1,2,3,1].
print: In ra danh sach.
insert 4 3: Chen gia tri 3 tai vi tri so 4, list=[1,2,3,1,3].
pop: Lay ra va loai bo phan tu cuoi cung cua danh sach, list=[1,2,3,1].
sort: Sap xep danh sach, list = [1,1,2,3].
print: In ra danh sach.
'''

n = int(input())
list = []
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        list.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':
        print(list)
    if cmd[0] == 'remove':
        list.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        list.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        list.sort()
    elif cmd[0] == 'pop':
        list.pop()
    elif cmd[0] == 'reverse':
        list.reverse()
