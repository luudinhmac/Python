lst = list(map(int, input("nhap cac phan tu cach nhau boi dau cach: ").split()))


# element_max = 0
# count_max =0
# for item in lst:
#     count =0
#     for element in lst:
#         if element ==item:
#             count +=1
#             #print(f"Đếm tại {element} = {count}")
#     if count > count_max:
#         count_max = count
#         element_max = item

# print(f"Phần tử {element_max} xuất hiện nhiều nhất với {count_max} lần")



# sử dụng hàm
max= 0
max_element = None
for i in lst:
    a =lst.count(i)
    if a > max:
        max = a
        max_element = i
print(f"{max_element} : {max}")

