# Python-Study
Python Online  Editor
======================
      https://repl.it/
      https://codelabs.developers.google.com/


The names you use when creating these labels need to follow a few rules:
=======================================================================                                                  
    1. Names can not start with a number.
    2. There can be no spaces in the name, use _ instead.
    3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
    4. It's considered best practice (PEP8) that names are lowercase.
    5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), 
       or 'I' (uppercase letter eye) as single character variable names.
    6. Avoid using words that have special meaning in Python like "list" and "str"      

Numbers
=======
      Integer
      Float
      Expression -> +, -, *, /, %, //, **, num * 0.5
      
      # Addition
      print(2 + 1)
      # Substraction
      print(2 - 1)
      # Multiplication
      print(2 * 2)
      # Division
      print(3 / 2)
      # Floor Division
      print( 7 // 4)
      # Modulo
      print(7 % 4)
      # Powers
      print(2 ** 3)
      # Can also do roots this way
      print(4 ** 0.5)
      # Order of Operations followed in Python
      print(2 + 10 * 10 + 3)
      # Can use parentheses to specify orders
      print((2 + 10) * (10 + 3))
      # Let's create an object called 'a' and assign it the number 5
      a = 5
      a = a + a
      print(a)
      a = 20
      a = a + a
      print(a)



Varible Assignments
====================
      - Python uses dynamic typing, meaning you can reassign variables to different data types
      - Variable assignment follows name = object, where a single equals sign = is an assignment operator
      - Determining variable type with type()
String - Immutable,cannot be changed
====================================
      1.) Creating Strings
      2.) Printing Strings
      3.) String Indexing and Slicing
      4.) String Properties
      5.) String Methods
      6.) Print Formatting
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

      # s = 'abcdefghijk'
      # print(s[2:9:3])
      # 2-start index
      # 9-end index
      # 3-count index
      # Output - cfi

      s = 'abcdefghijk'
      print(s[2:9:3])

String Formatting
=================
      player = 'Thomas'
      points = 33

      # Concatenation
      print('Last night,'+player+ 'scored' + str(points)+'points.')

      # String Formatting
      f'Last night, {player} scored {points} points'

      # Formatting with placeholders
      print("I'm going to inject %s here. " %'something')

      # Multiple items by placing them inside a tuple after % operator
      print("I'm going to inject %s text here, and %s text here." %('some','more'))

      x,y = 'some','more'
      print("I'm going to inject %s text here, and %s text here." %(x,y))

      # %r and repr() -including quotation marks and any escape charaters
      print('He said his name was %s.' %'Fred')
      print('He said his name was %r.' %'Fred')

      print('I once caught a fish %s.' %'this \tbig')
      print('I once caught a fish %r.' %'this \tbig')

      # %s operator converts whatever it sees into a string, including integers and floats. The %d operator converts numbers to integers first, without rounding
      print('I wrote %s programs today.' %3.75)
      print('I wrote %d program today.' %3.75)

      # Padding and Precision of Floating Point Numbers
      print('Floating point numbers: %5.2f' %(13.144))
      print('Floating point numbers: %1.0f' %(13.144))
      print('Floating point numbers: %1.5f' %(13.144))
      print('Floating point numbers: %5.2f' %(13.144))

      # Multiple Formatting
      print('First: %s, Second: %5.2f, Third:%r' %('hi!',3.1415,'bye!'))
      # Formatting with .format() method
      print('This is a string with an {}'.format('insert'))
      #  Inserted objects can be called by index position
      print('The {2} {1} {0}'.format('fox','brown','quick'))
      # Inserted objects can be assigned keywords:
      print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))
      # Inserted objects can be reused, avoiding duplication
      print('A %s saved is a %s earned.' %('penny','penny'))
      print('A {p} saved is a {p} earned.'.format (p='penny'))

      # Alignment, padding and precision with .format()
      # Within the curly braces you can assign field lengths, left/right alignments, rounding parameter
      print('{0:8} | {1:9}'.format('Fruid','Quality'))
      print('{0:8} | {1:9}'.format('Apples',3.))
      print('{0:8} | {1:9}'.format('Oranges', 10))

      # By default, .format() aligns text to the left, numbers to the right. You can pass an optional <,^, or > to set a left, center or right alignment
      print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
      print('{0:<8} | {1:^8} | {2:>8}'.format(22,34,56))

      #  can precede the aligment operator with a padding character
      print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
      print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

      # Field widths and float precision are handled in a way similar to placeholders
      print('This is my ten-character, two-decimal number:%10.2f' %13.579)
      print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))

      # Formatted String Literals (f-strings)
      #  f-strings offer several benefits over the older .format() string method described above
      name = 'Fred'
      print(f"He said his name is {name}.")
      # Pass !r to get the string representation
      print(f"He said his name is {name!r}.")

      # Float formatting follows "result: {value:{width}.{precision}}"
      # .format() method you might see {value:10.4f}, with f-strings this can become {value:{10}.{6}}
      num = 23.45678
      print("My 10 character, four decimal number is:{0:10.4f}".format(num))
      print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

      # f-strings, precision refers to the total number of digits, not just those following the decimal. This fits more closely with scientific notation and statistical analysis. Unfortunately, f-strings do not pad to the right of the decimal, even if precision allows it
      num = 23.45
      print("My 10 character, four decimal number is:{0:10.4f}".format(num))
      print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

      # use .format() method syntax inside an f-string
      num = 23.45
      print("My 10 character, four decimal number is:{0:10.4f}".format(num))
      print(f"My 10 character, four decimal number is:{num:10.4f}")
      
List-mutable,can be canged -> other languages like array
==============================
      1.) Creating lists
      ===================
            my_list = [1, 2, 3]
            print(my_list)
      2.) Indexing and Slicing Lists
      ==============================
            my_list = ['one','two','three',4,5]
            print(my_list[0])
            print(my_list[:3])
      3.) Basic List Methods
      =======================
            list1 = [1, 2, 3]
            list1.append('append me!')
            list1.pop(0)
            list1.sort()
            list1.reverse()
      4.) Nesting Lists
      ===================
            lst_1=[1,2,3]
            lst_2=[4,5,6]
            lst_3=[7,8,9]
            matrix = [lst_1,lst_2,lst_3]
            matrix[0][0]
            
      5.) Introduction to List Comprehensions
      =======================================
            first_col = [row[0] for row in matrix]
            print(first_col)
Dictionaries -> other languages like hash tables
=============
      1.) Constructing a Dictionary
      ==============================
            my_dict = {'key1': 'value1','key2':'value2'}
      2.) Accessing objects from a dictionary
      =======================================
            my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
            print(my_dict['key3'])
            print(my_dict['key3'][0])
            print(my_dict['key3'][0].upper())
            print(my_dict['key1'])
            my_dict['key1'] = my_dict['key1'] - 123
            print(my_dict['key1'])

      3.) Nesting Dictionaries
      ========================
            d = {'key1':{'nestkey':{'subnestkey':'value'}}}
            print(d['key1']['nestkey']['subnestkey'])
      4.) Basic Dictionary Methods
      ============================
            d = { 'key1':1,'key2':2,'key3':3}
            print(d.keys())
            print(d.values())
            print(d.items())
Tuples - Immutable,cannot be changed
=========
      1.) Constructing Tuples
      ==========================
            t = (1, 2, 3)
            t = ('one', 1,'one')
      2.) Basic Tuple Methods
      ======================
            print(t.index('one'))
            print(t.count('one'))
            
      3.) Immutability
      ================
             t[0] = 'change' -error
             t.append('nope') -error
             
      4.) When to Use Tuples
      =======================
            -tuples are not used as often as lists in programming, but are used when immutability is necessary
            -If in your program you are passing around an object and need to make sure it does not get changed, then a tuple becomes your solution. 
            -It provides a convenient source of data integrity
         
 Sets 
 ===
      x = set()
      x.add(1)
      x.add(2)
      x.add(1), output -> {1,2}
      - Sets are an unordered collection of unique elements
      - can cast a list with multiple repeat elements to a set to get the unique elements
            # Create a list with repeats
            list1 = [1,1,2,2,3,4,5,6,1,1]
            # Cast as set to get unique values
            set(list1) , Output -> {1, 2, 3, 4, 5, 6}
            
 Booleans
 ===========
      -Python comes with Booleans (with predefined True and False displays that are basically just the integers 1 and 0). It also has a placeholder object called None
      # Set object to be a boolean
      a = True
      # Output is boolean
      1 > 2, Output -> False
      # None placeholder
      b = None
      
 Files
 =====
      - w+  = create new text file, next time write ,overwrite to text file
      - a+ = append to existing text file,If the file does not exist, one will be created
      - # Open the text.txt we made earlier
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
       
   ========================================
       
       with open('abc.txt',mode='w') as f:
       f.write('I created this file!')

      with open('abc.txt',mode='r') as f:
           print(f.read())
           
   ============================================
   
      myfile=open('test1.txt',mode='w')
      myfile.write('Hello World')
      myfile.close()
Comparison Operators
=======================
      Equal
            1 == 2
      Not Equal
            1 != 2
      Greater Than
            1 > 2
      Less Than
            1 < 2
      Greater Than or Equal to
            1 >= 2
      Less than or Equal to
            1 <= 2
 Chained Comparison Operators
 =============================
      print (1 < 2 > 5)
      print( 1 < 2 or 2 > 5)
      print( 1 < 2 and 2 > 5)
Python Statements
==================
      if x:
          if y:
              code-statement
      else:
          another-code-statement
if, elif, else Statements
=========================
      if case1:
            perform action1
      elif case2:
          perform action2
      else: 
          perform action3
For Loop
========
      for item in object:
          statements to do stuff
while Loops
===========
      while test:
           code statements
      else:
          final code statements
 break, continue, pass
 ======================
     -  break: Breaks out of the current closest enclosing loop.
     -  continue: Goes to the top of the closest enclosing loop.
     - pass: Does nothing at all.
         while test: 
                code statement
                if test: 
                    break
                if test: 
                    continue 
         else:
Useful Operators
==================
      range
      enumerate
      zip
      in operator
      not in
      min and max
      random library -two useful functions -> randint(0,100), shuffle(mylist)
      input
      
 Function
 =======
      - The return keyword allows you to actually save the result of the output of a function as a variable.
      - The print() function simply displays the output to you, but doesn't save it for future use
      def print_result(a, b):
            print(a+b)

      def return_result(a,b):
          return a+b

      print_result(10,2)
      
 Lambda Expresssion
 ==================
      - map
      - filter
      
      def splicer(mystring):
          if len(mystring) % 2 == 0:
              return 'even'
          else:
              return mystring[0]

      mynames = ['shwe','sin','htay']
      print(list(map(splicer, mynames)))
      ====================================
      def check_even(num):
          return num % 2 ==0
      nums = [0,1,2,3,4,5,6,7,8,9,10]
      print(list(filter(check_even,nums)))
      
   Scope - LEGB Rule:
   ==================

      L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

      E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

      G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

      B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
      
 *args and **kwargs
 =================
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
       myfunc_test(fruit='cherries',juice='orange','eggs','spam')
       
 OOP Concepts
 ============
      -In Python, everything is an object
      -User defined objects are created using the class keyword
      -An attribute is a characteristic of an object. 
      -A method is an operation we can perform with the object.
      -The syntax for creating an attribute is:
            self.attribute = something
      -There is a special method called:
            __init__()
      -Inheritance is a way to form new classes using classes that have already been defined
      -Polymorphism refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety        of different objects might be passed in
      -Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax
            __init__(),
            __str__(),
            __len__() and 
            __del__() 

