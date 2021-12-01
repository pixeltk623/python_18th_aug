# class Car():
# 	car_color = "Blue"
# 	car_model = "BMW"
# 	car_price = 56446546

# 	def getCarPrice(self):
# 		return "Our Car Price is "+ str(self.car_price)

# 	def getMyCarName(self):
# 		print("My Name is Sharvan kumar")

# 	def getMyRollNumber(self):
# 		print("13AEI015")

# 	def getCollegeName(self):
# 		return "GIET GUNUPUR"

# objectOfCar = Car()

# # print(objectOfCar)

# # objectOfCar.car_color = "Red"
# # print(objectOfCar.car_color)
# # print(objectOfCar.getCarPrice())
# objectOfCar.getMyCarName()
# objectOfCar.getMyRollNumber()
# print(objectOfCar.getCollegeName())
	
# 		


# class Employee():
# 	__emp_name = "Sharvan"

# 	def __getEmpName(self):
# 		print(self.__emp_name)

# 	def getMyFullName(self):
# 		self.__getEmpName()

# objectOfEmp = Employee()

# # print(objectOfEmp)
# # print(objectOfEmp.getEmpName())
# objectOfEmp.getMyFullName()

# class Employee():
# 	def getName(self):
# 		print("Hello Kumar")


# objectN = Employee()

# objectN.getName()

# // Access Modifier 
# 1. Public => Fn or Member var  => inside and outside 
# 2. Private => inside class __
# 3. Protected => Child class  _


# class Employee():
# 	name = "Kumar"
# 	__salary = 456464

# 	def getUserSalary(self):
# 		return "My salary is "+str(self.__salary)

# 	def __getEmployeeSalary(self):
# 		#print(self.__salary)
# 		return self.__salary

# 	def getAllSalary(self):
# 		return self.__getEmployeeSalary()

# objectN = Employee()

# print(objectN.name)

# # print(objectN.salary)

# print(objectN.getUserSalary())

# print(objectN.getAllSalary())

class Employee():

	__baseSalary = None

	def __init__(self, name, email, mobile, base):
		self.name = name
		self.email = email
		self.mobile = mobile
		self.__baseSalary = base


	def getAllUserDetails(self):
		return {"name": self.name, "email": self.email, "mobile":self.mobile}

		#return {}

	def getGrossSalary(self):
		return self.__baseSalary
		
	# def setName(self, name):
	# 	self.name = name
	# def setEmail(self, email):
	# 	self.email = email
	# def setMobile(self, mobile):
	# 	self.mobile = mobile

	# def getName(self):
	# 	print(self.name)
	# def getEmail(self):
	# 	print(self.email)
	# def getMobile(self):
	# 	print(self.mobile)

name = "S Kumar"
email = "S@gmail.com"
mobile = "9835401515"
base = input("Salary: - ")

objectN = Employee(name, email, mobile, base)

print(objectN.getAllUserDetails())

print(objectN.getGrossSalary())

# objectN.setName(name)

# objectN.getName()


