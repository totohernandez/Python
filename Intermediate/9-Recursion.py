n = 7
fact = 1 
while n > 0:
    fact = fact * n
    n -= 1
print(fact)

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number
print(factorial(7))

#Fibonacci Sequence
# Fn = Fn-1 + Fn-2
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144... 

#Without Recursion 

def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a
print(fibonacci(10))

#With Recursion 
#The method with recursion can take too much time, stackoverflow error
#Exponential runtime complexity 

def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return (fibonacci2(n-1) + fibonacci2(n-2))
print(fibonacci2(10))

