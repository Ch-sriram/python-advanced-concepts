class PlayerCharacter:
    # class object attribute, common to all the instances of this class
    membership = True

    '''
    we can refer to membership, which is a class object attr, 
    using self.membership or using PlayerCharacter.membership,
    because it is not an instance of the object that's created
    from this class, it is a member attribute of this class and
    it will be a common attribute for all the objects 
    instantiated from this class.
    '''

    # constructor
    def __init__(self, name, age):
        if self.membership: # if PlayerCharacter.membership:
            # attributes are unique to each instance
            self.name = name 
            self.age = age

    def run(self):
        # to access the instance attributes, every method inside the class takes in a self parameter
        print(f'run started by {self.name}')
        return 'done'

p1 = PlayerCharacter('ram', 25)
print(p1.membership)  # True
p1.run()
PlayerCharacter.membership = False

p2 = PlayerCharacter('roop', 24)
print(p2.membership)  # False
print(p2.name)  # AttributeError

'''

Output:
------
True
run started by ram
False
Traceback (most recent call last):
  File "attr_method.py", line 33, in <module>
    print(p2.name)  # AttributeError
AttributeError: 'PlayerCharacter' object has no attribute 'name'

'''
