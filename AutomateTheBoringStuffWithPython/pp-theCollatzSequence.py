def collatz(number):
    list = []
    list.append(number)
    while(number != 1):    
        if (number % 2 == 0):
            number = number//2
            list.append(number)
        else:
            number = number*3 + 1
            list.append(number)
    print(list)

print('Enter a number:')
input = int(input())
collatz(input)
