'''
We achieve the functionality of closures using the nonlocal 
keyword in python. The following example depicts the concept 
of closures in python.

Read more about closures from here: 
1. https://github.com/Ch-sriram/JavaScript/blob/master/JS-Objects-Functions-Advanced/scripts/closure.js
2. https://github.com/Ch-sriram/JavaScript/blob/master/JS-Objects-Functions-Advanced/assets/closure.pdf
'''

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)
    
    inner()
    print('outer:', x)

outer()

'''
Output:

inner: nonlocal
outer: nonlocal

------------------------------------------------------------

If we comment out line #10, then, we will have the following 
output:

inner: nonlocal
outer: local
'''