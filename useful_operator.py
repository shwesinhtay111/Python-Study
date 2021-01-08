print(range(0, 12))

# Notice how 11 is not included, up to but not including 11, just like slice notation!
print(list(range(0,11)))
# Third parameter is step size!
# step size just means how big of a jump/leap/step you 
# take from the starting number to get to the next number.

print(list(range(0,11,2)))

# enumerate
index_count = 0
for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1

# Notice the tuple unpacking!

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

# zip 
# Notice the format enumerate actually returns, let's take a look by transforming it to a list()
print(list(enumerate('abcde')))

# can use the zip() function to quickly create a list of tuples by "zipping" up together two lists
mylist1 = [1, 2, 3, 4]
mylist2 = ['a', 'b','c', 'd']
print(zip(mylist1,mylist2))
print(list(zip(mylist1,mylist2)))

for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))

# in operator
# use it to quickly check if an object is in a list
print('x' in ['x', 'y', 'z'])
print('x' in [1, 2, 3])

#  combine in with a not operator, to check if some object or variable is not present in a list.
print('x' not in ['x','y','z'])
print('x' not in [1, 2, 3])

# min and max
mylist = [10, 20, 30, 40, 100]
print(min(mylist))
print(max(mylist))

# random library, show two useful functions
from random import shuffle
# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
shuffle(mylist)
print(mylist)

# Return random integer in range [a, b], including both end points.
from random import randint
print(randint(0,100))

# input
input('Enter Something into this box:')