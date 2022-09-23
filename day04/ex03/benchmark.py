
import timeit
import sys
from functools import reduce

def squares_sum_with_loop(some_number):
    result = 0
    for i in range(int(some_number) + 1):
        result += i ** 2
    
    return result

def sum_it(prev, current):
        return (prev + current **2)

def squares_sum_with_reduce(some_number):
    
    n = range(int(some_number) + 1)
 
    return reduce(sum_it, n)


if __name__ == '__main__':

    if len(sys.argv) == 4:

        if sys.argv[1] == 'loop':
            try:
                print(timeit.timeit(lambda: squares_sum_with_loop(int(sys.argv[3])), number=int(sys.argv[2])))
            except:
                raise Exception ('Something went wrong')

        elif sys.argv[1] == 'reduce':
            try:
                print(timeit.timeit(lambda: squares_sum_with_reduce(int(sys.argv[3])), number=int(sys.argv[2])))
            except:
                raise Exception ('Something went wrong')
    else:
        raise Exception ('Wrong arguments')
