# return duplicates from the list below using comprehensions
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Instead of the foll. code, do something else using comprehensions
# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)

print(list(set([char for char in some_list if some_list.count(char) > 1])))

'''
Output:
------
['b', 'n']
'''