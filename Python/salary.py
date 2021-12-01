class SalaryT():
	
	covid = 5000
	pt = 200
	tax = 0
	pf = 0
	def __init__(self,name,baseSalary):
		self.baseSalary = baseSalary
		self.name = name

	def calculateDa(self):
		if self.baseSalary<4000:
			return 0
		else:
			return (self.baseSalary*10)/100

	def calculateHra(self):
		if self.baseSalary<4000:
			return 0
		else:
			return (self.baseSalary*25)/100

	def calculateCa(self):
		if self.baseSalary<4000:
			return 0
		else:
			return (self.baseSalary*5)/100

	def calculateMedical(self):
		if self.baseSalary<4000:
			return 0
		else:
			return (self.baseSalary*2.5)/100

	def totalEarningSalary(self):
		if self.baseSalary>=4000:
			return (self.calculateDa()+self.calculateHra()+self.calculateCa()+self.calculateMedical()+self.covid)
		else:
			return 0
	
	def calculateTaxes(self):
		if self.baseSalary>=4000:
			if self.baseSalary>=20000:
				self.tax = (self.baseSalary*2.5)/100
			elif self.baseSalary>=30000:
				self.tax = (self.baseSalary*4.5)/100
			elif self.baseSalary>=40000:
				self.tax = (self.baseSalary*7)/100
			else:
				self.tax = 0
		else:
			self.tax = 0

		return self.tax

	def calculatePf(self):

		if self.baseSalary>=4000:
			if self.baseSalary>=20000:
				self.pf = (self.baseSalary*9)/100
			else:
				self.pf = 0
			return self.pf
		else:
			return  0


	def totalDeducation(self):
		if self.baseSalary>=4000:
			return (self.calculatePf()+self.calculateTaxes()+self.pt)
		else:
			return 0

	def calculateGrossSalary(self):
		return (self.totalEarningSalary() + self.totalDeducation())


	def takeHomeSalary(self):
		return (self.calculateGrossSalary() - self.totalDeducation())

name = input("Enter Your Name: ")
baseSalary = int(input("Enter Your Basic Salary: "))

# name = "Sharvan"
# baseSalary = 4000

objectT = SalaryT(name, baseSalary)

print("Earning " , objectT.totalEarningSalary())
print("Deducation " , objectT.totalDeducation())
print("Gross Salary " , objectT.calculateGrossSalary())
print("Take Home " , objectT.takeHomeSalary())