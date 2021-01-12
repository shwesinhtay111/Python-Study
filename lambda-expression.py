def square(num):
    return num**2
my_nums = [1,2,3,4,5]
print(map(square, my_nums))

# To get the results, either iterate through map() 
# or just cast to a list
print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]

mynames = ['shwe','sin','htay']
print(list(map(splicer, mynames)))

# filter function
def check_even(num):
    return num % 2 ==0
nums = [0,1,2,3,4,5,6,7,8,9,10]
print(list(filter(check_even,nums)))

def squarel(num): return num**2
print(squarel(2))

square = lambda num: num*2
print(square(2))

print(list(map(lambda num: num ** 2, my_nums)))

print(list(filter(lambda n: n % 2 == 0,nums)))

print(lambda s: s[0])
print(lambda s: s[::-1])
print(lambda x,y : x + y)