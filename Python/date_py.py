# import datetime

# from datetime import date

# # print(datetime)

# currentTimeDate = datetime.datetime.now()



# timestamp = date.fromtimestamp(1637156598)


# a = date(2019, 4, 13)

# print(a);

# print(timestamp)

# exit()

# # x = datetime.datetime(2018, 6, 1)

# # print(x.year)

# # print(x.strftime("%B"))

# # datetime = dir(datetime)

# # print(datetime)
# datetime_object = datetime.datetime.today()

# print(datetime_object)

# print(currentTimeDate)

# exit()

# # print(currentTimeDate)

# # print(currentTimeDate.year)
# # currentDay = currentTimeDate.strftime("%A") # Full Day Name
# # currentDay = currentTimeDate.strftime("%a") # Short Day Name

# # print(type(currentDay))

# # print(currentDay.upper())

# # oldDate = 2020, 5, 17 2021/05/06 12:00:00


# # y = datetime.datetime(2021, 5, 17)

# # print(y)

# # year = input("Enter The Year: ")
# # month = input("Enter The Month: ")
# # day = input("Enter The day: ")

# # Year 4 

# # month 1 & 2 

# # day 1 & 2


# # if len(year)>0 and len(year)==4:
# # 	print("Sahi Hai")
# # else:
# # 	print("Wrong")


# # if len(month)>0 and  len(month)<3:
# # 	print("Sahi Hai")
# # else:
# # 	print("Wrong")

# # if len(day)>0 and  len(day)<3:
# # 	print("Sahi Hai")
# # else:
# # 	print("Wrong")


# # if(year.length>4) {
# # 	print("pz Enter Valid Year")
# # }

# # if len(year)>4:
# # 	print("pz Enter Valid Year")
# # else:
# # 	y = datetime.datetime(int(year), month, day)

# # 	print(y)


# # t1 = "32"

# # if int(t1)>31:
# # 	print("Wrong")
# # else:
# # 	print("Sahi hai")




# # if len(year)>0 and len(year)==4

# # if len(month)>0 and  len(month)<3:

# # if len(day)>0 and  len(day)<3


# # if (len(year)==4) and (len(month)>=1 and  len(month)<=2 and int(month)<13) and (len(day)>=1 and  len(day)<=2 and int(day)<32):
# # 	y = datetime.datetime(int(year), int(month), int(day))
# # 	print(y)
# # else:
# # 	# # if len(year)!=0 and len(year)!=4:
# # 	# # 	print("Year Wrong")

# # 	# # if len(month)==0 or  len(month)>2:
# # 	# # 	print("Month Wrong")

# # 	# # if len(day)==0 or len(day)>2:
# # 	# # 	print("Day Wrong")
	
# # 	# print("Error")

# # 	if month=='':
# # 		print("Month can not be blank")
# # 	else:
# # 		if int(month)>12:
# # 			print("Month is Not valid")
# # 		else:
# # 			if len(month)>2:
# # 				print("length Error")
# # 			else:
# # 				print(month)

import datetime
from datetime import date

# a = date(2019, 4, 13)
# print(a)

# curretDate = date.today()

# print(curretDate)

# timestamp = date.fromtimestamp(1637327446)
# print("Date =", timestamp)


# curretDate = date.today()

# print(curretDate)

# print(curretDate.year)
# print(curretDate.month)
# print(curretDate.day)


from datetime import time

# a = time(19,11,11)

# a = time(19,11,11, 234566)

# a = time(hour=19, minute=15, second=16, microsecond = 234566)

# print(a)

# print(a.hourt)
# print(a.minute)
# print(a.second)
# print(a.microsecond)

from datetime import datetime

# a = datetime(year=2018, month = 11, day=28, hour=11,minute=11,second=11,microsecond=5465)

# print(a)

# print(a.year)
# print(a.month)
# print(a.day)



# print(a.hour)
# print(a.minute)
# print(a.second)
# print(a.microsecond)


# t1 = date(year = 2018, month = 7, day = 12)
# t2 = date(year = 2017, month = 12, day = 23)

# t3 = t1 - t2
# print("t3 =", t3)


# t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
# t5 = datetime(year = 2017, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t4 - t5
# print("t6 =", t6)

# from datetime import timedelta


# t1 = timedelta(weeks = 2, days = 0, hours = 0, seconds = 0)
# t2 = timedelta(days = 14, hours = 0, minutes = 0, seconds = 0)
# t3 = t1 - t2

# print("t3 =", t3)

# now = datetime.now()

# print(now)

# t = now.strftime("%H:%M:%S")

# s1 = now.strftime("%d/%m/%Y, %H:%M:%S")


# print(t)

# print(s1)

# import pytz

# local = datetime.now()
# print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

# tz_NY = pytz.timezone('America/New_York') 


# americaTime = datetime.now(tz_NY)

# print(americaTime)


# tz_London = pytz.timezone('Europe/London')
# datetime_London = datetime.now(tz_London)
# print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

