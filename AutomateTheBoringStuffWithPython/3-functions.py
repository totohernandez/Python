# #Functions 

# # built in functions
# import pyperclip

# pyperclip.copy('Hello World!')
# print(pyperclip.paste())

# # def statements with parameters
# def hello(name):
#     print('Hello ' + name)

# # return values and return statements
# hello('Alice')
# hello('Bob')

# import random 

# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidely so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtfull'

# print('Think of a yes or no question, and press to see the Magic 8 Ball Fortune')
# input()
# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)
# #print(getAnswer(random.randint(1,9)))

# # Local and Global Scope
# # local - parameters and variables assigned in a called function 
# # global - variables assigned outside all functions

# spam = 42 # global scope

# def eggs():
#     spam = 42 # local variable

# print('Some code here')
# print('some more code.')

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

def spam():
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)
