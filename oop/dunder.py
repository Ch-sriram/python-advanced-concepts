'''
In python, there are these double underscore methods aka dunder
methods or magic methods, which are __str__(), __len__(), 
__add__(), __sub__(), __mul__(), etc. These methods are called
internally whenever we try to use the str(), len(), +, -, *, 
etc functions/operators on python objects.

The functionality of these dunder methods is defined be 
default, but if we want to change the definition, we can do so 
by overriding the dunder method's definition in a class as 
shown in the example below:
'''

class Toy:
    def __init__(self, color, company):
        self.color = color
        self.company = company

action_figure = Toy('red', 'Funskool')
print(str(action_figure))  # same as -> action_figure.__str__()

'''
We haven't overloaded the __str__() method, and so, we'd get 
the default output as where the class is defined and what the 
memory location of the object is.

Output:
------
<__main__.Toy object at 0x03019130>

'''

'''
In the same way, we can make another class and this time, we 
can define what will happen if we call str(), by overriding the
__str__() method inside the class. Remember that we can do that
because all the classes made in Python by default inherit the 
topmost class called object.
'''

class Toy2(Toy):  # same as -> class Toy2(object):
    def __init__(self, color, company):
        super().__init__(color, company)
        self.my_dict = {
            'color': self.color,
            'company': self.company
        }

    def __str__(self):
        return f'The toy is manufactured by {self.company} and it is {self.color} in colour'

    def __len__(self):
        return len(self.color)

    def __call__(self):  # called whenever we call a function
        return str(self)

    def __getitem__(self, index):
        return self.my_dict[index]

    def __add__(self, other):
        return len(self) + len(other)

    def __del__(self):
        print('deleted the object')

barbie_doll = Toy2('pink', 'Mattel Toys')

# str() is called automatically on any object that is to be printed on to the console.
print(barbie_doll)  # same as print(str(barbie_doll))
print(len(barbie_doll))  # if not defined, you'd get TypeError
print(barbie_doll())  # if __call__() not defined, we get NameError
print(barbie_doll['company'])  # if __getitem__() is not defined, we'd get a TypeError saying object is not subscriptable

some_doll = Toy2('peach', 'Mattel Toys')

# if __add__() not defined, we'd get the following error: TypeError: unsupported operand type(s) for +: 'Toy2' and 'Toy2'
print(barbie_doll + some_doll)  # 9 as len('pink') + len('peach') is 9

del barbie_doll  # won't give any info in the console if not __del__() is not defined

'''
Output:
------

The toy is manufactured by Mattel Toys and it is pink in colour
4
The toy is manufactured by Mattel Toys and it is pink in colour
Mattel Toys
9
deleted the object
deleted the object
'''
