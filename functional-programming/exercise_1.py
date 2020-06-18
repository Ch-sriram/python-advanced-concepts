from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(lambda item: item.capitalize(), my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
print(sorted(list(zip(my_strings, my_numbers)), key=lambda x: x[1]))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda item: item > 50, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
print(reduce(lambda acc, item: acc + item, my_numbers + scores))


'''
Output:
------
['Sisi', 'Bibi', 'Titi', 'Carla']
[('e', 1), ('d', 2), ('c', 3), ('b', 4), ('a', 5)]
[73, 65, 76, 100, 88]
456
'''