'''
In functional programming, we have pure functions, which are 
basically program(s) that take an input and produce an output 
not changing anything other than the given input.

The pure function never interacts with anything that's outside 
its own scope. Example:

# def multiply_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(multiply_by_2([1,2,3]))  # [2, 4, 6]

The multiply_by_2() function doesn't change what was given to it,
but only uses it to produce a new list that is returned to back.
'''

# so there are few pure functions provided by python which are
# map(), filter(), zip() & reduce().

# we'll see how we use map() now:
# syntax of map: map(action, iterable)
# the action is a function and iterable is any collection that
# can be iterated on.

def multiply_by_2(item):
    return item*2

print(map(multiply_by_2, [1, 2, 3]))  # returns a map object

# we convert the map object to list to get the required output we want:
print(list(map(multiply_by_2, [1, 2, 3])))  # [2, 4, 6]


'''
Output:
------
<map object at 0x009191C0>
[2, 4, 6]
'''
