'''
zip() function works kind of like a combiner of collections.

syntax: zip(iterable1, iterable2[, iterable3, iterable4, ...])
'''

# Example of zip:

my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [5, 4, 3]

tuple_list = (10, 20, 30)

print(list(zip(my_list, your_list)))
print(list(zip(my_list, tuple_list)))
print(list(zip(my_list, your_list, their_list)))


'''
The zip() function in the first look may note seem useful, but 
it's use is when we pick data from a database into lists.

To combine those lists into a single list of tuples which 
inturn replicate a database table, is a really powerful 
feature of the zip() function.
'''


'''
Output:
------
[(1, 10), (2, 20), (3, 30)]
[(1, 10), (2, 20), (3, 30)]
[(1, 10, 5), (2, 20, 4), (3, 30, 3)]
'''