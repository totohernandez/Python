import threading

def helloworld():
    print('Hello World!')

t1 = threading.Thread(target=helloworld)
t1.start()

def function1():
    for x in range(3):
        print('ONE')

def function2():
    for x in range(3):
        print('TWO')

# function1()
# function2()

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t2.start()

def hello():
    for x in range(3):
        print('hello')

t3 = threading.Thread(target=hello)
t3.start()

print('Test')

t3.join()
print('Another Text')