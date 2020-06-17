class User:
    # this class doesn't have an __init__
    def sign_in(self):
        return 'logged in'

    # we can have same method names, but in different instances
    # of the same class/sub-class, they can be overridden.
    # For example, attack() method is defined here, which is
    # again defined in Wizard and Archer classes too
    def attack(self):
        return f'do nothing'


# Wizard is subclass of User
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


# Demonstration of Polymorphism
def player_attack(obj):
    return obj.attack();

print(player_attack(w1))  # attacking with power of 50
print(player_attack(a1))  # attacking with arrows: arrows-left are 100

# Demo 2 of Polymorphism:
for obj in [w1, a1]:
    print(player_attack(obj))

'''
Output:
------

attacking with power of 50
attacking with arrows: arrows-left are 100
attacking with power of 50
attacking with arrows: arrows-left are 100
'''