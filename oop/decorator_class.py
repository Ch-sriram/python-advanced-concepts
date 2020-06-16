class PlayerCharacter:
    membership = True   # class object attribute

    # constructor
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute

    def run(self):
        print(f'run started by {self.name}')
        return 'done'

    # the way we can define common methods for all the objects
    # of this class is that we use decorators like @classmethod
    # or something like @staticmethod and then define the
    # the method with the specified description of the
    # decorator. For example:

    @classmethod
    def new_object(cls, num1, num2):
        '''
        1st param of a classmethod is always by convention 
        known as cls, which is used to create an instance 
        variable (object) of this class, which we will see 
        below.
        '''
        return cls('Teddy', num1 + num2)  # instantiated an object of type PlayerCharacter

    '''
    We also have @staticmethod which cannot create a new 
    instance of the class and therefore doesn't take in cls 
    by default and so, it can do normal stuff as shown below
    '''

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2
        


# usage of classmethod
print(PlayerCharacter.new_object(20, 30))  # memloc of object
p1 = PlayerCharacter('Ram', 25)
p2 = PlayerCharacter.new_object(2, 3)
print(p1.new_object(20, 5).name)  # Teddy
print(p2.age)  # 5

'''
We can see that the classmethod can be used by both the 
instance and the class itself and can be called to do what it's
defined to do.
'''


# usage of staticmethod
print(PlayerCharacter.adding_things(7, 3))  # 10

'''

Output:
------
<__main__.PlayerCharacter object at 0x008BA130>
Teddy
5
10

'''