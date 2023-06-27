test_dict = {'Python': {"a": 7, "b": 9, "c": 12},
             'with': {"a": 15, "b": 19, "c": 20},
             'TEK4.VN': {"a": 5, "b": 10, "c": 2}}

temp = []
for i in test_dict.values():
    print(i)
    for j in i:
        if j == 'c':
            temp.append(i[j])
print(temp)
