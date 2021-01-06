# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1': 'value1','key2':'value2'}

# Call values by their key
print(my_dict['key2'])

# dictionaries are very flexible in the data types they can hold
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict['key3'])
print(my_dict['key3'][0])
print(my_dict['key3'][0].upper())
print(my_dict['key1'])
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])

# Set the object equal to itself minus 123 
my_dict['key1'] -= 123
print(my_dict['key1'])

# Create a new Dictionary
d = {}
d['animal'] = 'Dog'
# Can do this with any object
d['answer'] = 42
print(d)

# Nesting with Dictionaries
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d['key1']['nestkey']['subnestkey'])

# Dictionary Method
d = { 'key1':1,'key2':2,'key3':3}
print(d.keys())
print(d.values())
print(d.items())