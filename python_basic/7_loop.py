# for loop/while loop

for i in range(2,0, -1):
    # range(start, stop, step)
    print(i)


liss= ["mac", "mai","minh"]
for i in range(len(liss)):
    print (i, liss[i])


k =0
while k< 5:
    print(k)
    k+= 1

print("==============while True============")

o = 8
while True:
    if o > 5 :
        print(o)
        break
    else:
        i+= 1