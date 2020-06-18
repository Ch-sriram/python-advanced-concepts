'''
Based on the name of the function, we can tell that filter(), 
will filter out the items from an iterable depending on the 
condition we give in the function.

We will see the example below:
'''

my_list = [1, 2, 3]

def only_odd(item):
    return item % 2 != 0


# syntax of filter: filter(action, iterable)
print(list(filter(only_odd, my_list)))  # [1, 3]