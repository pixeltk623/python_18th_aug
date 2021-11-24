class Car():
	car_color = "Blue"
	car_model = "BMW"
	car_price = 56446546

	def getCarPrice(self):
		return "Our Car Price is "+ str(self.car_price)

	def getMyCarName(self):
		print("My Name is Sharvan kumar")

	def getMyRollNumber(self):
		print("13AEI015")

	def getCollegeName(self):
		return "GIET GUNUPUR"

objectOfCar = Car()

# print(objectOfCar)

# objectOfCar.car_color = "Red"
# print(objectOfCar.car_color)
# print(objectOfCar.getCarPrice())
objectOfCar.getMyCarName()
objectOfCar.getMyRollNumber()
print(objectOfCar.getCollegeName())
	
		