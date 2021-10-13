import socket
s = socket.socket()
print('socket Created')

s.bind(('localhost',8989))
s.listen(3)
print('waiting for connection')

while True:
	c, addr = s.accept()

	name = c.recv(1024).decode()

	print("Connected with ", addr, name)
	
	c.send(bytes("Welcome to Kumar"+name, 'utf-8'))

	c.close()

