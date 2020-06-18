# we have list/set/dictionary comprehensions in python
# comprehensions are a quick way to create a list/set/dict in
# python, instead of creating a loop to append/add a bunch of
# items to a list/set/dict.

# Instead of doing the following:
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)  # ['h', 'e', 'l', 'l', 'o']

# we can write the foll. list comprehension
# syntax for list comprehensions:
# my_list = [expression for item in iterable <optional if condition>]
# meaning: for each item in the iterable, if the optional condition is true, evaluate the expression and add the produced value to my_list. See examples to understand.

my_list = [char for char in 'hello']
print(my_list)  # ['h', 'e', 'l', 'l', 'o']



# Another example: to create a list from 0-9:
my_list2 = [num for num in range(10)]
print(my_list2)


# Example: if we want to create a list from 0-9, but each value should be multiplied by 2.
# my_list3 = list(map(lambda item: item * 2, my_list2))
# we want to only use list comprehensions:
my_list3 = [num * 2 for num in range(10)]
print(my_list3)

# Example: if we want to keep only even numbers from a list of 0-99 that have been raised to power of 2 each.
my_list4 = [num ** 2 for num in range(100) if num % 2 == 0]
# meaning of the comprehension above: add num^2 iff num is even
print(*my_list4)

'''
Output:
------
['h', 'e', 'l', 'l', 'o']
['h', 'e', 'l', 'l', 'o']
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
0 4 16 36 64 100 144 196 256 324 400 484 576 676 784 900 1024 1156 1296 1444 1600 1764 1936 2116 2304 2500 2704 2916 3136 3364 3600 3844 4096 4356 4624 4900 5184 5476 5776 6084 6400 6724 7056 7396 7744 8100 8464 8836 9216 9604
'''