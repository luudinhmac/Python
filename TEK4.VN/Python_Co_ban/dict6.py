# sap xep tang dan theo diem, neu diem bang nhau thi theo ten alphabet
lists = [{"name": "Hung", "point": 10},
       {"name": "Giang", "point": 10},
       {"name": "Hieu", "point": 9}]

print(sorted(lists, key = lambda i: (i['point'], i['name'])))

# sorted_list = []
# for i in range(len(lists)):
#     for j in range(i + 1, len(lists)):
#         if lists[i]["point"] > lists[j]["point"]:
#             lists[i], lists[j] = lists[j], lists[i]
#         elif lists[i]["point"] == lists[j]["point"] and lists[i]["name"] > lists[j]["name"]:
#             lists[i], lists[j] = lists[j], lists[i]
# # sorted_list = lists
# print(lists)