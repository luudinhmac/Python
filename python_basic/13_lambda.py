# lambda :  small(one line) anonymous function - Hàm ẩn danh
# lambda arguments: expression

# example
test_lambda = lambda x: x+100
print(test_lambda(200))

#
list_samples = [-1,-5,-3,-8 , 1,2,0 ,5,1]
print(sorted(list_samples, key = lambda x : abs(x)))

#

list_coor = [(0,4), (1,4), (-3,5),(5,10)]
print(sorted(list_coor, key = lambda x : x[1]))

