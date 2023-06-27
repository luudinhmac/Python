from world import asia as a


def check_pr(numbers):
    not_prime = []
    prime = []
    for i in numbers:
        if a.vietnam.check_prime(i) == True:
            prime.append(i)
        else:
            not_prime.append(i)

    print(f"Number is a prime: {prime}")
    print(f"Number is not prime: {not_prime}")


arr = [1, 3, 4, 5, 6, 7, 8, 9, 12, 13]

check_pr(arr)


