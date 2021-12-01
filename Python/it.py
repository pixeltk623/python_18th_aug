#myTuple = ("apple", "banana", "cherry")

# print(myTuple)

# for x in myTuple:
# 	print(x)

# newT = iter(myTuple)

# # print(newT)

# print(next(newT))

# print(next(newT))


# print(next(newT))
# print(next(newT))


# class Company():
# 	_profit = 465465
# 	def __init__(self, name, email):
# 		self.name = name
# 		self.email = email

# 	def getCompanyName(self):
# 		return self.name

# class Employee(Company):
# 	def __init__(self, name, email):
# 		super(Company, self).__init__()
# 		self.name = name
# 		self.email = email

# 	def getTotalProfit(self):
# 		return self._profit
		


# ob = Employee("ABC",54654)

# print(ob.getTotalProfit())
# print(ob.getCompanyName())



# Python Function to print leaders in array

def printLeaders(arr,size):
	
	for i in range(0, size):

		for j in range(i+1, size):
			if arr[i]<=arr[j]:
				break
		if j == size-1: # If loop didn't break
			print(arr[i]),

# Driver function
arr=[6, 7, 4, 3, 5, 2, 8, 9 , 1]
printLeaders(arr, len(arr))

