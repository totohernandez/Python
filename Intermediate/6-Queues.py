import queue

# First in first out
# 1, 2, 3, 4, 5 
# 1
# 2, 3, 4, 5
# 2
# 3, 4, 5 
# 3
# 4, 5 
# 4
# 5


q = queue.Queue()

numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    q.put(number)

print(q.get())
print(q.get())

# Last in first out

q2 = queue.LifoQueue()

numbers = [1,2,3,4,5,6,7]
for x in numbers:
    q2.put(x)

print(q2.get())

# Priority queue

q3 = queue.PriorityQueue()

q3.put((2, "Hello World!"))
q3.put((11, 99))
q3.put((5, 7.5))
q3.put((1, True))

while not q.empty():
    print(q3.get())

