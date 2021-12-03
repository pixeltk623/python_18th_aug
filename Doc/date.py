import datetime

datetime_object = datetime.datetime.now() #Get Current Date and Time

# print(datetime_object)

# print(datetime.date.today())  #Get Current Date

# print(dir(datetime)) #We can use dir() function to get a list containing all attributes of a module.


# Commonly used classes in the datetime module are:

# date Class
# time Class
# datetime Class
# timedelta Class

# d = datetime.date(2021,9,9)

# print(d)

from datetime import date

# d = datetime.date(2021,9,9)

# print(d)

# print("Current Date : ", date.today())

# print(date.fromtimestamp(1326244364))
# today = date.today()
# print(today)

# print(today.year)
# print(today.month)
# print(today.day)


from datetime import time

# a = time(11,34,56)

# print(a.hour)
# print(a.minute)
# print(a.second)

# print(a)



from datetime import datetime, date

# a = datetime(2018,11,11, 23, 55, 59, 342380)

# print(a)



# a = datetime(2017, 11, 28, 23, 55, 59, 342380)
# print("year =", a.year)
# print("month =", a.month)
# print("hour =", a.hour)
# print("minute =", a.minute)

# print("timestamp =", a.timestamp())


# t1 = date(2021, 9, 26)
# t2 = date(2021, 8, 26)

# t3 = t1-t2

# print(t3)

# t4 = datetime(year = 2021, month = 7, day = 12, hour = 7, minute = 9, second = 33)
# t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t4 - t5


# print("t6 =", t6)
# print("type of t3 =", type(t3)) 
# print("type of t6 =", type(t6))  



from datetime import timedelta

# t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
# t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)

# t3 = t1 - t2

# print(t3)


# t1 = timedelta(seconds = 33)
# t2 = timedelta(seconds = 54)
# t3 = t1 - t2

# print("t3 =", t3)
# print("t3 =", abs(t3))


# t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
# print("total seconds =", t.total_seconds())


# now = datetime.now()

# s1 = now.strftime("%d/%m/%Y, %H:%M:%S")


# print("time:", s1)


# date_string = "21 June, 2018"
# print("date_string =", date_string)

# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)


# import pytz

# local = datetime.now()

# print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

# tz_NY = pytz.timezone('America/New_York') 
# datetime_NY = datetime.now(tz_NY)
# print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

# tz_London = pytz.timezone('Europe/London')
# datetime_London = datetime.now(tz_London)
# print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
