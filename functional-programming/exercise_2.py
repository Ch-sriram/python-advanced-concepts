# Small exercises on lambda expressions

# Square each element in the list using lambda expression
my_list = [5, 4, 3]
print(list(map(lambda item: item ** 2, my_list)))

# Sort the following list on the basis of the 2nd element in the tuple
my_list = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(my_list, key=lambda tup: tup[1]))


'''
Output:
------
[25, 16, 9]
[(10, -1), (0, 2), (4, 3), (9, 9)]
'''
