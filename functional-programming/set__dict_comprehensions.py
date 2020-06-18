# examples on set and dict comprehensions

# EXAMPLES OF SET COMPREHENSION
# making a set comprehension is actually really easy
# instead of a list, we'll just use a set notation as follows:

my_list = [char for char in 'hello']
my_set = {char for char in 'hello'}
print(my_list)
print(my_set)

my_list1 = [num for num in range(10)]
my_set1 = {num for num in range(10)}
print(my_list1)
print(my_set1)

my_list2 = [num ** 2 for num in range(50) if num % 2 == 0]
my_set2 = {num ** 2 for num in range(50) if num % 2 == 0}
print(my_list2)
print(my_set2)


# EXAMPLE OF DICT COMPREHENSIONS

# Example 1:
simple_dict = {'a': 1, 'b': 2}
my_dict = {k: v ** 2 for k, v in simple_dict.items()}
# for each of the key:value pair in the simple_dict, we raise the value by the power of 2 and add it to my_dict
print(my_dict)

# Example 2: if we only want the even values from simple_dict to be in my_dict, then, we have the following dict comprehension
my_dict2 = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict2)


# Example 3: If we want to make a dict from a list where the list item is the key and item*2 is the value in the dict, using dict comprehension:
my_dict3 = {item: item * 2 for item in [1, 2, 3]}
print(my_dict3)

'''
Output:
------
['h', 'e', 'l', 'l', 'o']
{'o', 'h', 'l', 'e'}
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304]
{0, 256, 1024, 2304, 4, 900, 1156, 16, 144, 400, 784, 1296, 1936, 36, 676, 1444, 64, 576, 1600, 196, 324, 2116, 100, 484, 1764}
{'a': 1, 'b': 4}
{'b': 4}
{1: 2, 2: 4, 3: 6}
'''
