# Creating a String
name ='shwe sin'
address = "magway"
age = "I'am 20 years old"
print(name, address, age)

# Printing a String
print('Use \n to print a new line')

# String Basics
print(len('Shwe Sin'))

# String Indexing
s = 'Hello World'
print(s)
print(s[0])
print(s[1:])
print(s[:3])
print(s[-1])

print(s[-2:])
print(s[:-2])
print(s[1:])
print(s[:3])

# Grab everything, but go in steps size of 1
print(s[::1])

# Grab everything, but go in step sizes of 2
print(s[::2])

# We can use this to print a string backwards
print(s[::-1])

# String Properties
s = 'Hello World'
s = s + ' concatenate me!'
print(s)

letter = 'z'
print(letter *25)

# Basic Built-in String methods
print(s.upper())
print(s.lower())
print(s.split())
print(s.split('W'))

# Print Formatting
print('Insert another string with curly brackets: {}'.format('The inserted string'))
print('Hello {}'.format('Shwe Sin'))
