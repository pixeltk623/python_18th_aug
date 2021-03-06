# List
# Lists are used to store multiple items in a single variable.
# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# thislist = ["apple", "banana", "cherry"]

# print(thislist[2])

#Allow Duplicates

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]

# print(thislist)

#List Length

# print(len(thislist))

# List Items - Data Types

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# print(type(list1))

# print(type(list2))

# print(type(list3))

# list4 = list(["apple", "banana", "cherry"])
# print(list4)

#List Constructor

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

# print(thislist)

# allNumber = [1, 5, 7, 9, 3]

# print(allNumber.count(1))

# Negative Indexing
# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-3])


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]

# if "applek" in thislist:
# 	print("Hai")

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]

# thislist.insert(1, "asdsa")
# print(thislist)

# Append Items
# To add an item to the end of the list, use the append() method:
# thislist.append("asdadasds")

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# Remove Specified Item
# The remove() method removes the specified item.


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# newlist = [expression for item in iterable if condition == True]


# newlist = [x for x in range(10)]

# print(newlist)

# newlist = [x for x in range(10) if x < 5]

# newlist = [x.upper() for x in fruits]

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = ['hello' for x in fruits]

# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# thislist = [100, 50, 65, 82, 23]

# # thislist.sort() 

# thislist.sort(reverse = True)
# print(thislist)

# print(thislist)




# list1 = ["cc","a","aaa","eeee","dddddd"]
# print(list1)

# list1.sort(key=len)

# print(list1)

# list2 = [[2,9],[1,10],[3,7]]

# list2.sort()

# def sortByFun(element):
# 	return element[1]

# list2.sort(key=sortByFun)

# print(list2)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]

# # copyList = thislist.copy()

# copyList = list(thislist)

# print(copyList)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)


# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# n_list = ["Happy", [2, 0, 1, 5]]


# print(n_list[1][0])

# print(n_list[0][1])

# print(n_list[1][3])

# 	List

# => Lists are used to store multiple items in a single variable.
# 	=> List Items

# => List items are ordered, changeable, and allow duplicate values.

# => List items are indexed, the first item has index [0], the second item has index [1] etc.

# for x in range(1,11):
	
# 	if x==5:
# 		continue
# 	print(x)

# for x in range(1,11):
	
# 	if x==5:
# 		break
# 	print(x)

# exit()




studentList = ["Sharvan","Meet","Akasht","Darshan","Ram","ABC","XYZ"]

# print(type(studentList))

# studentList.append("Test")
# studentList.append("Test")
# studentList.append("Test")
# studentList.append("Test")

# studentList.extend("Hello")
# print(studentList)

# print(studentList[-1])
# print(studentList[-2])
# print(studentList[-3])
# print(studentList[-4])

#print(studentList[2:5])

# print(studentList[2:])

# print(studentList[:3])

# print(studentList[-3:-1])

# print(studentList[-2:])

# print(studentList[:-4])


# studentList[3] = "ABC"
# print(studentList[3])

# print(studentList)

# typeOfStudent = ["Sharvan",12345,True,25.33]

# #studentList = ["Sharvan","Meet","Akasht","Darshan","Sharvan","Meet","Akasht","Darshan"]


# for x in range(len(studentList)):
# 	if studentList[x]=='Meet':
# 		print("Hello " + studentList[x] + " How r u ?")
# 		#print(studentList[x])
# 	else:
# 		print(studentList[x])

# print(len(studentList))

# print(studentList[0])
# print(studentList[1])

# print(studentList)

# print(typeOfStudent)




# allEvenNo = []
# for x in range(1,101):
# 	if x%2==0:
# 		#print(x)
# 		allEvenNo.append(x)


# print(allEvenNo)


# newList = list(("Test","Hello"))

# print(newList)

# print(type(newList))
# listOfPrimeNumber = []
# for x in range(1,101):
# 	count = 0
# 	for y in range(1,x+1):
# 		if x%y==0:
# 			count = count+1
# 	if count==2:
# 		listOfPrimeNumber.append(x)


# print(listOfPrimeNumber)

# print(studentList)

# studentList.remove("XYZ")

# print(studentList)

# studentList.pop()

# studentList.pop(1)

# print(studentList)


# del studentList

# print(studentList)

# studentList.clear()

# print(studentList)
# i = 0
# while (i<len(studentList)):
# 	print(studentList[i])
# 	i = i+1

# for x in studentList:
# 	if x=='Darshan':
# 		print("Yes")


# for x in studentList:
# 	# print(x.lower())
# 	print(x.upper())


# x = [x.lower() for x in ["A", "B", "C"]]

# print(x)




# [x.upper() for x in ["a", "b", "c"]]


# exit()

# studentList1 = ["sharvan","Meet","akasht","Darshan","ram","aBC","xYZ", "Ant"]

# newList = []
# for x in studentList1:
# 	newList.append(x.lower())

# print(newList.count("meet"))
# print(newList)

# exit()
# studentList1.lower()

# print(studentList1)

# exit()

# print(studentList1.count("Meet"))

# exit()

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list3 = [True, False, True]
	
# list1.extend(list2)
# list1.extend(list3)
# print(list1)

# exit()
# students = list(studentList1)

# print(students)

# exit()

# studentList2 = studentList1.copy()

# print(studentList1)

# print(studentList2)
# exit()

# studentList1.reverse()

# print(studentList1)
# exit()

# studentList1.sort(key = str.lower)

# print(studentList1)




# var = ['ant','bat','cat','Bat','Lion','Goat','Cat','Ant']
# var.sort(key = str.lower)

# print(var)


# #['ant', 'Ant', 'bat', 'Bat', 'cat', 'Cat', 'Goat', 'Lion']

# ['ant', 'Ant', 'bat', 'Bat', 'cat', 'Cat', 'Goat', 'Lion']

# exit()
# studentList = ["Banana", "Orange", "Kiwi", "cherry","Cat"]

# # print(studentList)

# studentList.sort(key = str.lower)

# print(studentList)

# rollNo = [171141,45,8,78,988,128]

# studentList.sort()

# studentList.sort(reverse=True)

# # rollNo.sort()

# rollNo.sort(reverse=True)

# print(rollNo)

# print(studentList)


studentList1 = ["sharvan","Meet","akasht","Darshan","ram","aBC","xYZ", "Ant"]

# studentList1.insert(9,"odd")

# print(studentList1)

# studentList1[2:4] = ["adsas","adsas"]

#print(studentList1)

# newlist = [x for x in studentList1 if 'a' in x]

# print(newlist)

# --------------------Tuple -----------------------

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

tuple1 = ("sharvan","Meet","akasht","Darshan","sharvan","Meet","akasht","Darshan")

thistuple  = tuple(("sharvan","Meet","akasht","Darshan"))

# print(thistuple)

# print(type(tuple1))

# print(tuple1)

# print(tuple1[1])
# print(tuple1[-1])
# print(tuple1[2:5])
# print(tuple1[:4])
# print(tuple1[2:])
# print(tuple1[-4:-1])

# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# tuple2 = list(tuple1)

# tuple2[1] = "Hello"

# print(tuple2)

# tuple1 = tuple(tuple2)

# print(tuple1)



# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists


# st = ("Sharvan","Sanjeev","Raushan")

# #(cse,it,aei) = st

# (cse,it,aei) = st

# print(cse)
# print(it)
# print(aei)


# Note: The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.

# st = ("Sharvan","Sanjeev","Sanjeev","Sanjeev","Raushan")
# st1 = ("asdas","asdasd")
# (cse,*it,aei) = st

# print(cse)
# print(it)
# print(aei)

# for x in st:
# 	print(x)


# print(st + st1)

# print(st*10)

# print(st.index("Raushan"))
# print(st.count("Sanjeev"))


# ------------SET-------------------

# Set items are unordered, unchangeable, and do not allow duplicate values.



thisSet = {"Sharvan","Sanjeev","Raushan"}

# thisSet = set(("Sharvan","Sanjeev","Raushan"));
# print(thisSet)

# print(type(thisSet))

# for x in thisSet:
# 	print(x)

# print("Sharvan" in thisSet)

# thisSet.add("shweta")

# print(thisSet)

# newSet = ("asdasd","kdsasa")

# mylist = ["kiwi", "orange"]

# thisSet.update(mylist)

# print(thisSet)


#thisSet.remove("Sharvan")

# Note: If the item to remove does not exist, remove() will raise an error.

# thisSet.discard("Sharvan")

# thisSet.pop()
# thisSet.clear()


# print(thisSet)

# del thisSet

# print(thisSet)


# There are several ways to join two or more sets in Python.

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

# set1 = {"a", "b" , "c"}
# set2 = {1, "b", 3}

# set3 = set1.union(set2)
#set1.update(set2)
# print(set3)

#print(set1)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)

# print(x)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)

# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)

# print(z)


# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)
# print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


# print(thisdict.get("brand"))

# #print(y)

# print(thisdict.keys())

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change



# car["color"] = "white"	

# print(x) #after the change

# car["color"] = "white"

# print(x) #after the change


x = thisdict.values()

print(x)