# Open the text.txt we made earlier
myfile = open('textfile.txt')
print(myfile)

# We can now read the file
print(myfile.read())

# But what happens if we try to read it again?
print(myfile.read())

# Seek to the start of file (index 0)
print(myfile.seek(0))

# Now read again
print(myfile.read())

# Readlines returns a list of the lines in the file
myfile.seek(0)
print(myfile.readlines())

# When you have finished using a file, it is always good practice to close it
myfile.close()

# Writing to a File
# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

myfile = open('test.txt','w+')
# Write to the file
myfile.write('This is a new line')
print(myfile.seek(0))
print(myfile.read())

# always do this when you're done with a file
myfile.close()  

# Appending to a File
my_file = open('textfile.txt','a+')
my_file.write('\nThis is text being appended to textfile.txt')
my_file.write('\nAnd another line here.')
print(my_file.seek(0))
print(my_file.read())

# Iterating through a File
for line in open('textfile.txt'):
 print(line)


 with open('textfile.txt',mode='r') as myfile:
     contents = myfile.read()
print(contents)


with open('abc.txt',mode='w') as f:
 f.write('I created this file!')

with open('abc.txt',mode='r') as f:
     print(f.read())
