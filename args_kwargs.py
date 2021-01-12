# function parameter starts with an asterisk, it allows for an arbitrary number of arguments
#  the function takes them in as a tuple of values
def myfunc(*args):
    return sum(args)*.05

print(myfunc(40,50,30))

# the word "args" is itself arbitrary - any word will do so long as it's preceded by an asterisk
def mytest(*spam):
    return sum(spam)*.05

print(mytest(30,40,50))

#  Python offers a way to handle arbitrary numbers of keyworded arguments. 
# Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs
def my_func(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")
        
print(my_func(fruit='pineapple'))
print(my_func())

# can pass *args and **kwargs into the same function, but *args have to appear before **kwargs
def myfunc_test(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' or '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
myfunc_test('eggs','spam',fruit='cherries',juice='orange')

# Placing keyworded arguments ahead of positional arguments raises an exception
# myfunc_test(fruit='cherries',juice='orange','eggs','spam')