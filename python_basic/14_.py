#MAP, FILTER, REDUCE
# map (func , object): transform object with func
# filter (func , object): filter object with you want
# reduce (func , object): return single value, func get 2 arg



list_temp = [1,4,5,23,32,35,124,24]
# def sum(x):
# return x + 2
# print(list(map(sum, list_temp))) # normal

# using lambda
print(list(map(lambda x: x*2 , list_temp)))

print(list(filter(lambda x: x % 2 == 1,list_temp)))

list1 =  [ x for x in list_temp if x % 2 ==1 ]
print(list1)

# reduce
from functools import reduce
print(reduce(lambda x,y : x if x< y else y, list_temp))
