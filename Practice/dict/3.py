#ex03
"""
Cho data 1 cửa hàng, dữ liệu kiểu như sau :
d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
    {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
    {"name":"Trung","phone":"555-3141","email":""},
    {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},
]

#1. Tìm tất cả user có số điện thoại kết thúc bằng 8
#2: tìm tất cả user o có địa chỉ email
"""

d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
    {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
    {"name":"Trung","phone":"555-3141","email":""},
    {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},
]

for i in d:
    phone_row =i['phone']
    if phone_row[-1]=='8':
        name_show=i['name']
        print('='*20)
        print(name_show)
        print(i['phone'])
        print(i['email'])
print("========Cac user co email ===================")

for j in d:
    em = j["email"]
    if em=="":
        print(j['name'])
        print(j['phone'])
        print(j['email'])
        print('='*20)