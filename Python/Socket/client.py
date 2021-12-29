import socket
import pickle

c = socket.socket()

c.connect(('192.168.29.180',3005))

<<<<<<< Updated upstream
listOfName = ["Sadsa","asdsad","asd"]

# email = input("Enter Your Email: ")
c.send(bytes(listOfName, 'utf-8'))
=======
y=[0,12,6,8,3,2,10] 
data=pickle.dumps(y)


print("Connecting")

email = input("Enter Your Email: ")
c.send(data)
>>>>>>> Stashed changes

print(c.recv(1024).decode())
