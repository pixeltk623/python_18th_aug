import socket
s = socket.socket()
#print("Socket Created");
s.bind(('192.168.29.180',3005))
s.listen(3)
print('waiting for connection')

while True:
	c, addr = s.accept()

	name = c.recv(1024).decode()

	print("Connected with ", addr, name)

	c.send(bytes("Welcome to "+name, 'utf-8'))

	c.close()


# 192.168.29.71

# 192.168.29.187

# Mysql -> Python
# MongoDB -> Python - 1
# File Handling 
# Date & Regix & Json - 1

# Class - 1

# Multithreading - 1

# 5


# Django 

# Js/Jquery - 1 

# 6 


# Login System 

# Crud






