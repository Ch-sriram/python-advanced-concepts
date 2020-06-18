'''
lambda expressions are one-time anonymous functions that we 
don't more than once. They're really useful for functions that 
we only use once, and they're really useful for occasions 
where we need a function for something really specific
'''

# syntax => lambda params: action_that_returns
# The params are the parameters to the anonymous function.
# The action is what we return from the function, note that
# we don't need to use a return statement.

# map() example

# Instead of the following function:
def multiply_by_2(item):
    return item * 2

print(list(map(multiply_by_2, [1, 2, 3])))


# we can do the same above thing using a lambda function:
print(list(map(lambda item: item * 2, [1, 2, 3])))



# filter() example
print(list(filter(lambda item: item % 2 != 0, [1, 2, 3, 4, 5])))

# reduce() example
from functools import reduce
print(reduce(lambda ac, item: ac + item, [1, 2, 3], 10))  # 16

'''
Output:
------
[2, 4, 6]
[2, 4, 6]
[1, 3, 5]
16
'''