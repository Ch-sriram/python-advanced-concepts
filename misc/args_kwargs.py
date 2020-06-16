'''
With a function we actually have special variables we use, which
are *args and **kwargs.

If we have to give more than 1 positional argument to a 
function, we use *args. For example, the following code will 
raise a TypeError:

        def super_func(args):
            return sum(args)

        super_func(1,2,3,4,5)

Error description: 
TypeError: super_func() takes in 1 positional argument but 5 were given


Now, for any function to take in a variable amount of arguments, 
we've to pass the arguments to *args in the function as shown 
below:
'''

def super_func(*args):
    print(args)     # (1, 2, 3, 4, 5) <- tuple
    print(*args)    # 1 2 3 4 5 <- tuple unpacked and spaced
    return sum(args)

print(super_func(1, 2, 3, 4, 5))    # 15 


'''
We can see that *args as the parameter to the super_func 
function takes in the parameters as a tuple. We generally name it
as *args, but we can technically name it as any name we want.

Moving on to **kwargs, (which stands for "Keyword Arguments") it 
is used for defining parameters while calling the function.

We can see the example below which uses both *args and **kwargs:
'''

def super_function(*args, **kwargs):
    print(args)     # (1, 2, 3, 4, 5)           <- tuple
    print(kwargs)   # {'num1': 5, 'num2': 10}   <- dict
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_function(1, 2, 3, 4, 5, num1=5, num2=10))


"""
PTR: There's an actual ordering recommended by python3 docs for 
defining the parameters in a function definition/call and it is:

         --------------first to last-------------------->
def func(positional_params, *args, default_args, **kwargs):
    # your code
"""