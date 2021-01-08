list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in list1:
    print(num)

for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Old number')

list_sum = 0
for sum in list1:
    list_sum = list_sum + num
print(list_sum)

# strings are a sequence so when we iterate through them we will be accessing each item in that string
for letter in 'This is a string.':
    print(letter)

# Tuple for loop
tup = (1, 2, 3, 4)
for t in tup:
    print(t)

list2 = [(1,2),(3,6),(7,9)]
for t in list2:
    print(t)
for (t1,t2) in list2:
    print(t2)

# Ditionary for loop
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

d.items()

for k,v in d.items():
    print(k)
    print(v)
#  to obtain a true list of keys, values, or key/value tuples, you can cast the view as a list
print(list(d.keys()))
# dictionaries are unordered, and that keys and values come back in arbitrary order.
print(sorted(d.values()))