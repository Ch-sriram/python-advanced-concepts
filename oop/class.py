# blueprint of the class
class BigObject:
    pass

obj1 = BigObject()  # instance of BigObject class
obj2 = BigObject()  # instance of BigObject class

print(obj1, obj2)   # memory location of obj1 and ob2
print(type(obj1), type(obj2))   # info about class type
print(isinstance(obj1, BigObject))  # True

'''
Output:

<__main__.BigObject object at 0x01599130> <__main__.BigObject object at 0x01599250>
<class '__main__.BigObject'> <class '__main__.BigObject'>
True
'''
