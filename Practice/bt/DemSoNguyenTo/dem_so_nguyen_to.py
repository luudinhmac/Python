with open("NGUYENTO.INP") as fi:
    n = fi.readline()
    lst = map(int, fi.readline().split())


def check_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

#1
# def count_prime(n, lst):
#     count = 0
#     for i in lst:
#         if check_prime(i):
#             count += 1
#     return count


# with open("NGUYENTO.OUT", "w") as fo:
#     fo.write(str(count_prime(n, lst)))


#2 list comprehension
lst_prime = [i for i in lst if check_prime(i)]

with open("NGUYENTO.OUT", "w") as fi:
    fi.write(str(len(lst_prime)))