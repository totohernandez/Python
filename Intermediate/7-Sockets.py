import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# PSP SOCK_STREAM
# UDP SOCK_DGRAM
s.bind(('127.0.0.1', 55555))
s.listen()

while True:
    client, address = s.accept()
    print("Conected to {}".format(address))
    client.send("You are conected!".econde())
    client.close()
