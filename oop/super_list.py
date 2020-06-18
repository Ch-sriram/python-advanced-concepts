'''
We can create a list data type on which we can add our own
functionalities. Let's say we will call it SuperList as defined
below:
'''

class SuperList(list):
    def __len__(self):
        return 1000  # no matter what the length of the actual list is, we can return it as 1000
    
    def __getitem__(self, index):
        return f'item at index={index} is {super().__getitem__(index)}'

sl = SuperList()

print(len(sl))  # 1000
sl.append(5)
print(sl[0])  # item at index=0 is 5
print(issubclass(SuperList, list))  # True


'''
Output:
------

1000
item at index=0 is 5
True
'''