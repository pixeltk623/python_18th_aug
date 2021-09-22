
#newNumber = 5
# userInput = int(input("Enter The Number: "))

# #print(type(userInput))
# #print(type(newNumber))

# #exit()
# sumOfNumber = 0
# if userInput<1:
# 	print("Inavlid Input")
# else:
# 	for i in range(1,userInput+1):
# 		sumOfNumber = sumOfNumber + i # 0 + 1 // 1 1 +2 = 3


# print(sumOfNumber)

# if sumOfNumber%2==0:
# 	print("Even No")
# else:
# 	print("Odd Number")


#nameOfUser = input("Enter Your Name : ")
# userInput = int(input("Enter The Number: "))

# i = 1
# sumOfNumber = 0
# while i<=userInput:
# 	sumOfNumber = sumOfNumber + i
# 	i = i+1


# print(sumOfNumber)

#123 = 1 + 2 + 3 = 5

userInput = int(input("Enter The Number: "))
sumOfDigits = 0
while userInput>0:
	rem = userInput%10 #3 2 
	sumOfDigits = sumOfDigits+rem # 3 + 2 +1 = 6
	# userInput /= 10
	userInput = int(userInput/10) #12


print(sumOfDigits) 












	