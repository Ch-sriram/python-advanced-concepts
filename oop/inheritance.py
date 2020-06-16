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

'''
Output:
------

logged in
attacking with power of 50
logged in
attacking with arrows: arrows-left are 100
'''
