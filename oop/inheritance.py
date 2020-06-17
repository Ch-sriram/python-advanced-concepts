class User:
    # this class doesn't have an __init__
    def sign_in(self):
        return 'logged in'


# this is the way to achieve inheritance. Wizard is subclass of USer
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        return f'attacking with power of {self.power}'

# Archer is also a derived/sub class of User 
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        return f'attacking with arrows: arrows-left are {self.num_arrows}'

w1 = Wizard('Merlin', 50)
a1 = Archer('Robinhood', 100)

print(w1.sign_in())  # logged in
print(w1.attack())  # attacking with power of 50
print(a1.sign_in())  # logged in
print(a1.attack())  # attacking with arrows: arrows-left are 100

# in python, we also have a useful function called isinstance()
# which can be used to check whether the object is the instance
# of the respective class, or not.
print(isinstance(w1, Wizard))  # True
print(isinstance(a1, Archer))  # True
print(isinstance(a1, Wizard))  # False
print(isinstance(w1, Archer))  # False

# Everything in python is an object, it literally means that
# every python data type like list, tuple, dict, etc and user-
# defined objects are an instance of the top-most super class
# called object.

# Therefore, all of the follwing will result True
print(isinstance(w1, object))  # True
print(isinstance(a1, object))  # True
print(isinstance([], object))  # True
print(isinstance(tuple, object))  # True
print(isinstance(dict, object))  # True
print(isinstance(set, object))  # True

'''
Output:
------

logged in
attacking with power of 50
logged in
attacking with arrows: arrows-left are 100
True
True
False
False
True
True
True
True
True
True
'''