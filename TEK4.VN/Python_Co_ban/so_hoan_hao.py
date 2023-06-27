# so hoan hao la so nguyen duong ma tong cac uoc so cua no
# lon gap 2 lan so do,
"""
1 cach dinh nghia khac la tong cac uoc cua no(tru no) bang chinh no
"""


def perfect_number(a, b):
    for i in range(a, b+1):
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s += j
        if s == i:
            print("{} is a perfect number".format(i))


a = int(input())
b = int(input())
print("Below are all perfect numbers between {} and {}:".format(a, b))
perfect_number(a, b)
