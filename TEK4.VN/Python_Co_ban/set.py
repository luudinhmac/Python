# items = {1, 2, 3, 4, 5, 8, 9, 12, 15, 17,
#          21, 25, 27, 31, 32, 38, 40, 44, 48, 50}
# n = int(input())
# il = len(items)
# customer = []
# for i in range(n):
#     each_customer = set([int(x) for x in input().split()])
#     customer.append(each_customer)

# print(customer)
# count = 0
# for each_customer in customer:
#     # giao item va customer / so mat hang cua alice
#     if len(items & each_customer)/len(items) > 0.4:
#         count += 1
# print(count)
# if count / n > 0.5:
#     print("YES")
# else:
#     print("NO")



# Khai báo tập hợp các mặt hàng mà Alice mua
items = {1, 2, 3, 4, 5, 8, 9, 12, 15, 17, 21, 25, 27, 31, 32, 38, 40, 44, 48, 50}

# Đọc vào số người dùng khác n
n = int(input("Nhập số người dùng khác: "))

# Khai báo biến đếm số người dùng có trên 40% mặt hàng trùng với Alice
count = 0

# Lặp qua n người dùng khác
for i in range(n):
    # Đọc vào tập hợp các mặt hàng mà người dùng thứ i mua
    user_items = set(map(int, input().split()))
    # Tính tỉ lệ phần trăm các mặt hàng trùng với Alice
    percentage = len(items.intersection(user_items)) / len(items)
    # Nếu tỉ lệ phần trăm lớn hơn hoặc bằng 40%, tăng biến đếm lên 1
    if percentage > 0.4:
        count += 1

# Kiểm tra xem Alice có phải là khách hàng điển hình hay không
# Nếu biến đếm lớn hơn nửa số người dùng khác, Alice là khách hàng điển hình
if count > n / 2:
    print("YES")
# Ngược lại, Alice không phải là khách hàng điển hình
else:
    print("NO")