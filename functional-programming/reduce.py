'''
The reduce() function isn't provided by python directly.
reduce() function is present inside the functools package, from
which we import the reduce() function.

In the functools library, we have functional tools that we can 
use to work with functions and callable objects.
'''

from functools import reduce

# syntax for reduce: reduce(function, iterable[, init_value_of_the_internal_acc])

# The reduce function has an accumulator that it takes as the
# first parameter and the next parameter is the item from the
# iterable. The value of accumulator by default is 0.

# whatever we return from the function is stored in the
# accumulator parameter, and this is the main reason why we
# use the reduce() function.

def accumulator(acc, item):
    return acc + item

my_list = [1, 2, 3]
print(reduce(accumulator, my_list))  # same as -> reduce(accumulator, my_list, 0)
print(reduce(accumulator, my_list, 10))  # 16

# reduce() is really powerful and under the hood, map() and
# filter() functions actually use the reduce() method

'''
Output:
------
6
'''
