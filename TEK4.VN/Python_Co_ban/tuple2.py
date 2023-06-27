test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
K = int(input())
#print([t for t in test_list if all(e % K == 0 for e in t)])  #comprehention
div = True
res =[]
for i in test_list:
    for j in i:
        if j % K !=0:
           div = False
           break
    if div == True: 
        res.append(i)

print(res)