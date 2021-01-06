# Create list
my_list = [1, 2, 3]
print(my_list)

# lists can actually hold different object types
my_list = ['A string', 23, 100.22, 'o']
print(my_list)
#  len() function will tell you how many items are in the sequence of the list
print(len(my_list))

# Indexing and Slicing
my_list = ['one','two','three',4,5]
print(my_list[0])
print(my_list[:3])
new_list = my_list + ['new item']
print(new_list)

#  use the * for a duplication method similar to strings
print(new_list*2)

# Basic List Methods
list1 = [1, 2, 3]
list1.append('append me!')
print(list1)

# Use pop to "pop off" an item from the list
list1.pop(0)
print(list1)

# Assign the popped element, remember default popped index is -1
popped_item = list1.pop()
print(popped_item)

#  use the sort method and the reverse methods to also effect your lists
new_list = ['a','b','x','b','c']

# Use reverse to reverse order (this is permanent!)
new_list.reverse()
print(new_list)

# Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
new_list.sort()
print(new_list)

# Nesting Lists
# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
print(matrix)

# Grab first item in matrix object
matrix[0]

# Grab first item of the first item in the matrix object
matrix[0][0]

# List Comprehensions
# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
print(first_col)
