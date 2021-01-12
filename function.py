def say_hello():
    print('hello')
say_hello()

# Accepting parameters
def greeting(name):
    print(f'Hello {name}')
greeting('Shwe Sin')

# Using return
def add_num(num1, num2):
    return num1 + num2

print(add_num(4, 5))

# Can also save as variable due to return
result = add_num(4,5)
print(result)

# Input two strings
print(add_num('one','two'))


# The return keyword allows you to actually save the result of the output of a function as a variable. The print() function simply displays the output to you, but doesn't save it for future use
def print_result(a, b):
    print(a+b)

def return_result(a,b):
    return a+b

print_result(10,2)

# You won't see any output if you run this in a .py script
return_result(10,5)

my_result = print_result(20,20)
print(type(my_result))

my_result = return_result(20,20)
print(my_result)
print(my_result + my_result)

def even_check(number):
    return number % 2 == 0
print(even_check(21))

def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False
print(check_even_list([1,2,3]))
print(check_even_list([1,1,1]))

def check_even_lists(num_list):
    even_num = []
    for num in num_list:
        if num % 2 == 0:
            even_num.append(num) 
        else:
            pass
    return even_num

print(check_even_lists([1,2,3,4,5,6]))

# ** Recall we can loop through a list of tuples and "unpack" the values within them**
stock_prices = [('AAPL',200),('GOOG',300),('MSFT',400)]

for item in stock_prices:
    print(item)

for stock,price in stock_prices:
    print(stock)

for stock,price in stock_prices:
    print(price)

# functions often return tuples, to easily return multiple results for later use
work_hours = [('Abby',100),('Billy',400),('Cassie',800)]
def employee_check(work_hours):
       
# Set some max value to intially beat, like zero hours
    current_max = 0
# Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
        
        # Notice the indentation here
    return (employee_of_month,current_max)
print(employee_check(work_hours))

from random import shuffle
mylist = [' ','O',' ']
def shuffle_list(mylist):
# Take in list, and returned shuffle versioned
    shuffle(mylist)
    return mylist
print(mylist)
print(shuffle_list(mylist))

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Pick a number: 0, 1 or 2:')
    return int(guess)
print(player_guess())

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)
mylist = ['', 'O', '']
mixedup_list = shuffle_list(mylist)
guess = player_guess()

check_guess(mixedup_list,guess)