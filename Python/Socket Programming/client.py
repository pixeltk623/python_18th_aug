import socket
c = socket.socket()

c.connect(('localhost',8989))
name = input("Enter Your Name")
c.send(bytes(name, 'utf-8'))
print(c.recv(1024).decode())

