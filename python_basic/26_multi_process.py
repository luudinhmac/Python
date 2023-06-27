# Process

import time
import multiprocessing
from multiprocessing import process
result = []
def square(numbers):
    global result
    time.sleep(10)
    print("Caculate square of numbers")
    for x in numbers:
        result.append(x*x)
    print("Result is: " + str(result))
# def cube(numbers):
#     time.sleep(10)
#     print("Caculate cube of numbers")
#     for x in numbers:
#         print("Cube: ", x*x*x)

if __name__ == "__main__":
    arr = [1,3,4,6,2]
    process1 = multiprocessing.Process(target=square, args = (arr,))
    #process2 = multiprocessing.Process(target=cube, args =(arr,))

    process1.start()
    # process2.start()
    process1.join()
    # process2.join()
    print("Result is: " + str(result))
    print("Done process")