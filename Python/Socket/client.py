import socket

c = socket.socket()

c.connect(('localhost',3003))

listOfName = ["Sadsa","asdsad","asd"]

# email = input("Enter Your Email: ")
c.send(bytes(listOfName, 'utf-8'))

print(c.recv(1024).decode())
