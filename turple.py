# Constructing Turples
t = (1, 2, 3)
print(len(t))

# Mix object types
t = ('one', 1,'one')
print(t)
print(t[0])
print(t[-1])

# Basic Turple Methods
print(t.index('one'))
print(t.count('one'))

# Immutability
# t[0] = 'change' -error
# t.append('nope') -error
