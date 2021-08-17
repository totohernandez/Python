#List data type

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

#Getting value in a list with indexes
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

#Negative indexes
print(spam[-1])
print(spam[-3])

# Sublists with slices
print(spam[0:4])
print(spam[1:3])
print(spam[:2])
print(spam[1:])

# list length 
print('Hello ' + spam[0])
print(len(spam))

# Changing values in a list with indexes
spam[0] = 'dog'
print(spam)

# List concatenation and replication
spam2 = [1, 2, 3] + ['A', 'B', 'C']
print(spam2)
spam3 = spam2 + [4, 5, 6] + ['D', 'E', 'F']
print(spam3)

# Removing Values from lists with del statement
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)

#list function
hi = list('Hello')
print(list)
print(hi[0] + hi[1] + hi[2] + hi[3] + hi[4])
# in and not in operator
print('cat' in spam)
print('cat' not in spam)
print('dog' in spam)
print('dog' not in spam)


# Working with lists 
# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) +1) + '(or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name] #list concatenation
#     for name in catNames:
#         print(' ' + name)
        

# Using for Loops with lists
for i in range(4):
    print(i)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is ' + supplies[i])

# Multiple Assigment 
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

size, color, disposition = cat
print(size)

# Augmented Assigment Operators
# += 1; -= 1, *= 1, /=1, %=1
spam = 42
spam = spam + 1
print(spam)

spam = 42 
spam += 1
print(spam)
