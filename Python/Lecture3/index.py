
# a = "asds"
# print(a.isnumeric())

# exit()
# if a.isnumeric()==False:
# 	print("Hello")
# else:
# 	print("Hi")
#hello
# exit()
# number = 12345
# rev = 0
# while number>0:
# 	rem = number%10
# 	rev = (rev*10)+rem #5
# 	number = int(number/10)


# print(rev) #543

# userInput = int(input("Enter The Number: "))
# tempNumber = userInput
# sumOfCube = 0
# while userInput>0:
# 	rem = userInput%10
# 	sumOfCube = sumOfCube + (rem*rem*rem)
# 	userInput = int(userInput/10)


# if sumOfCube==tempNumber:
# 	print("Number is Armstrong ")
# else:
# 	print("Number is Not Armstrong ")

# print(sumOfCube)

#a + b

# def printName():
# 	print("Hello This is Sharvan")


# printName()
# printName()
# printName()
# printName()


# def sumOfTwoDigits():
# 	a = int(input("Enter The First Number: "))
# 	b = int(input("Enter The First Number: "))

# 	return a+b

# print(sumOfTwoDigits())

# test = "Hello This is Kumar"

# def printUserInput():
# 	return "This is Test"

# def sumOfTwoDigits(x,y):
# 	return x+y

# hello = printUserInput()
# sumNew = sumOfTwoDigits(x,y)


# x = a
# y = b


# def getAllNewName(firstName="Tops", lastName="Baroda"):
# 	return "Hello This is "+firstName+" and Last Name is "+lastName


# print(getAllNewName("A"))
# print(getAllNewName("A","B"))
# print(getAllNewName())
# print(getAllNewName("B"))
# print(getAllNewName("C"))

# def countOfDigits(num):
# 	return len(countOfDigits)


# print(countOfDigits(4566))

# exit()

def multipleOfEachNumber(num):
	return (num*num*num)

def armstrongNumber(number=0):
	if number.isnumeric()==True:
		numberIs = int(number)
		tempNumber = numberIs
		sumOfCube = 0
		if numberIs<1:
			return "Invalid Number"
		else:
			while numberIs>0:
				rem = numberIs%10
				sumOfCube = sumOfCube + multipleOfEachNumber(rem)
				numberIs = int(numberIs/10)

			if sumOfCube==tempNumber:
				return tempNumber , " is Armstrong Number"
			else:
				return tempNumber , " is Not Armstrong Number"
	else:
		return "Pz Do Not Put Bekar Number"
userInput = input("Enter The Number: ")

print(armstrongNumber(userInput))
