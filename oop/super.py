# # by default, every class inherits from the object class
# class User: # same as -> class User(object):
#     def __init__(self, email):
#         self.email = email
    
#     def sign_in(self):
#         return f'logged in'

# # Wizard is a subclass of User
# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         return f'attacking with power of {self.power}'

# w1 = Wizard('Merlin', 60)
# print(w1.email)  # AttributeError

'''
One way to get around this error is that we can have another 
argument inside the Wizard's __init__() method called email, 
and then simply create an email attribute in Wizard itself.

But that way is just more code without actually using the super
class we already have, which is the User class. Therefore, to 
use the User class, we will simply make use of super() method
from the __init__() method of Wizard class, to call the 
__init__() method of User class as follows:
'''

# by default, every class inherits from the object class


class User:  # same as -> class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return f'logged in'

# Wizard is a subclass of User


class Wizard(User):
    def __init__(self, name, power, email):
        # we can call the __init__() method of User in 2 ways:
        super().__init__(email)  # same as User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        return f'attacking with power of {self.power}'


w1 = Wizard('Merlin', 60, 'merlin123@gmail.com')
print(w1.email)  # merlin123@gmail.com


'''
To know what the Wizard instance has access to, we can
introspect an object using the dir() function as follows:
'''

print(dir(w1))


'''
Output:
------

merlin123@gmail.com
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']

'''


'''
We can see that we have access to attack(), email, name, power
and the sign_in() methods/attributes from both the Wizard and
User class.
'''