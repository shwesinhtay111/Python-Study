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
         
