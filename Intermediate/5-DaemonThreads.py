import threading
import time

path = "5-DaemonText.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("5-DaemonText.tx", "r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()

