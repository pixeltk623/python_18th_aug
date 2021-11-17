import datetime

from datetime import date

# print(datetime)

currentTimeDate = datetime.datetime.now()



timestamp = date.fromtimestamp(1637156598)


a = date(2019, 4, 13)

print(a);

print(timestamp)

exit()

# x = datetime.datetime(2018, 6, 1)

# print(x.year)

# print(x.strftime("%B"))

# datetime = dir(datetime)

# print(datetime)
datetime_object = datetime.datetime.today()

print(datetime_object)

print(currentTimeDate)

exit()

# print(currentTimeDate)

# print(currentTimeDate.year)
# currentDay = currentTimeDate.strftime("%A") # Full Day Name
# currentDay = currentTimeDate.strftime("%a") # Short Day Name

# print(type(currentDay))

# print(currentDay.upper())

# oldDate = 2020, 5, 17 2021/05/06 12:00:00


# y = datetime.datetime(2021, 5, 17)

# print(y)

# year = input("Enter The Year: ")
# month = input("Enter The Month: ")
# day = input("Enter The day: ")

# Year 4 

# month 1 & 2 

# day 1 & 2


# if len(year)>0 and len(year)==4:
# 	print("Sahi Hai")
# else:
# 	print("Wrong")


# if len(month)>0 and  len(month)<3:
# 	print("Sahi Hai")
# else:
# 	print("Wrong")

# if len(day)>0 and  len(day)<3:
# 	print("Sahi Hai")
# else:
# 	print("Wrong")


# if(year.length>4) {
# 	print("pz Enter Valid Year")
# }

# if len(year)>4:
# 	print("pz Enter Valid Year")
# else:
# 	y = datetime.datetime(int(year), month, day)

# 	print(y)


# t1 = "32"

# if int(t1)>31:
# 	print("Wrong")
# else:
# 	print("Sahi hai")




# if len(year)>0 and len(year)==4

# if len(month)>0 and  len(month)<3:

# if len(day)>0 and  len(day)<3


# if (len(year)==4) and (len(month)>=1 and  len(month)<=2 and int(month)<13) and (len(day)>=1 and  len(day)<=2 and int(day)<32):
# 	y = datetime.datetime(int(year), int(month), int(day))
# 	print(y)
# else:
# 	# # if len(year)!=0 and len(year)!=4:
# 	# # 	print("Year Wrong")

# 	# # if len(month)==0 or  len(month)>2:
# 	# # 	print("Month Wrong")

# 	# # if len(day)==0 or len(day)>2:
# 	# # 	print("Day Wrong")
	
# 	# print("Error")

# 	if month=='':
# 		print("Month can not be blank")
# 	else:
# 		if int(month)>12:
# 			print("Month is Not valid")
# 		else:
# 			if len(month)>2:
# 				print("length Error")
# 			else:
# 				print(month)