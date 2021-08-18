# Boolean Values

spam = True
print(spam)

comparisonOp = 42 == 42
# comparisonOp = 2 != 2
print(comparisonOp)

operator = (4 < 5) and (5 < 6)
print(operator)

# Conditions If 
name = 'Bob'
if name == 'Alice':
    print("Hi, Alice")
print('Done')

#Conditions if else 
password = 'anakyn'
if password == 'anakyn':
    print('Access granted')
else:
    print('wrong password')

print('Enter your name: ')
name = input()
if name == 'Toto':
    print('Hello Toto')
else:
    print("Hello Stranger")

# Conditions if elif 
name = 'Toto'
age = 25
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kid.')
elif age > 2000:
    print('You are inmortal')
elif age > 100:
    print('You are not Alice, granma.')
else:
    print('GG')

# While loops 
span = 0
while span < 5:
    print('while')
    span = span + 1

span = 0
if span < 5:
    print('if')
    span = span + 1

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you')

# Continue statement 
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

while True:
    print("Who are you?")
    name = input()
    if name != 'Jose':
        continue
    print('Hello, Jose. What is the password?')
    password = input()
    if password == 'besugo':
        break
print('Acess granted.')

#for Loop
print('My name is')
for i in range(5):
    print('Jimy five times (' + str(i) + ')')

total = 0 
for num in range(101):
    total = total + num
print(total)

for i in range(12, 16):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)

import random
for i in range(5):
    print(random.randint(1, 10))

# import modules 
import random, sys, os, math

while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')