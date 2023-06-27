print("Vietnamese")
def check_prime(i):
    if i <  2:
        return False
    else:
        for k in range(2, i):
            if i%k ==0:
                return False
            else: return True

