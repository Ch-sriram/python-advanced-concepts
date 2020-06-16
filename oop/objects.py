class PlayerCharacter:

    # __init__ is a dunder method that acts as a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'executed run()'

player1 = PlayerCharacter('Ram', 25)
player2 = PlayerCharacter('Roop', 24)

print(player1)        # memory location of the object
print(player1.run())  # run \nexecuted run()

print(player2)
print(player2.run())
print(player2.age)

# We can also add properties to certain instances as follows:
player2.attack = 40
print(player2.attack)

'''
Output:
------

<__main__.PlayerCharacter object at 0x00E29118>
run
executed run()
<__main__.PlayerCharacter object at 0x00E29160>
run
executed run()
24
40
'''