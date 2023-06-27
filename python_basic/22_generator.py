# What is Generator?


# binh thuong
# def square_nums(list_nums):
#     list_temp = []
#     for x in list_nums:
#         list_temp.append(x*x)
#     return list_temp
# list_num = [1,5,12]
# print(square_nums(list_num))

# Generator
# def square_nums(list_nums):
#     for x in list_nums:
#         yield x*x
# list_num = [1,5,12]
# print(list(square_nums(list_num)))

# generated = square_nums(list_num)
# print(next(generated))
# print(next(generated))
# print(next(generated))
# new_generator = (x*x for x in list_num)
# print(list(list(new_generator)))


#

import random
import time
from memory_profiler import profile

branchs = ['BMW', 'Vinfast', 'Toyota', 'Mez', 'Lexus', 'Lamboghini']
engines = ['2.0', '3.0', '4.0', 'v8', 'v12']

# list
# @profile
# def car_list(num_people):
#     results = []
#     for i in range(num_people):
#         car = {
#             'id': i,
#             'name': random.choice(branchs),
#             'engine': random.choice(engines)
#         }
#         results.append(car)
#     return results

# generator
@profile
def car_generator(num_people):
    for i in range(num_people):
        car = {
            'id': i,
            'name': random.choice(branchs),
            'engine': random.choice(engines)
        }
        yield car

# Test memory usage
# t1 = time.time()
# people = car_list(1000000)
# t2 = time.time()
# print(f'List Took {t2-t1} seconds')

t1 = time.time()
people = list(car_generator(1000000))
t2 = time.time()
print(f'Generator Took {t2-t1} seconds')

# command to run test memory 
# python -m memory_profiler