import socket

c = socket.socket()

c.connect(('localhost',3003))


email = input("Enter Your Email: ")
c.send(bytes(email, 'utf-8'))

print(c.recv(1024).decode())
