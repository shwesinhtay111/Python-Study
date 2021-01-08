x = 0
while x < 10:
    print('x is currently:', x)
    print('x is still less than 10, adding 1 to x')
    x += 1
else:
    print('All Done!')
# a continue being printed out as we continue through the outer while loop
x = 0
while x < 10:
    print('x is currently:', x)
    print('x is still less than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('x == 3')
    else:
        print('continuing...')
        continue
# else statement wasn't reached and continuing was never printed!
x = 0
while x < 10:
    print('x is currently:', x)
    print('x is still less than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('Breaking because x == 3')
        break
    else:
        print('continuing....')
        continue
# A word of caution however! It is possible to create an infinitely running loop with while statements
# # DO NOT RUN THIS CODE!!!! 
while True:
    print("I'm stuck in an infinite loop!")