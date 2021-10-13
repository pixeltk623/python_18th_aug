# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

#set1 = {"list","tuple","set","dict"}

# set1 = {"list"}

# print(len(set1))

# print(type(set1))

# set1 = set(("list","tuple","set","dict"))

# print(type(set1))
# print(set1)


# for x in set1:
# 	print(x)

# print("list" not in set1)


# set1 = {"list","tuple","set","dict","dict","list","tuple","set","dict","dict"}

# print(set1)

# set1 = {"list","tuple","set","dict"}

# set2 = {True,True,False}

# set3 = {1,2,3,4}

# set4 = {"list","tuple",True,5,9.8}

# print(set2)

# set1 = {"list","tuple","set","dict","list"}

# del set1

# print(set1)

# set1.clear()

# print(set1)

#set1.remove("asdsa")
# set1.discard("list")

# print(set1)

#set1.remove("list")
#set1.discard("list")
# set1.pop()
# set1.pop()
# set1.pop()
# set1.pop()

#print(set1)

#set1.add("Hello")

# set1.add("HelloYU")


# set2 = {"abc","def"}

# list1 = ["1","2","7"]

# tuple1 = ("sda","klii") 

# set1.update(tuple1)

#set1.update({"Test"})

# set1.add("Hello")

# print(set1)

#set1.update(set2)


# set1 = {"list","tuple","set","dict"}

# set2 = {5,"Test", "tuple"}

# set3 = set1.union(set2)

# print(set3)

# set1.intersection_update(set2)

# print(set1)


# set3 = set1.intersection(set2)

# print(set3)

# set1.symmetric_difference_update(set2)

# print(set1)

# set3 = set1.symmetric_difference(set2)


# print(set3)



# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

# mydict = {
# 	"name": "sharvan",
# 	"email": "s@gmail.com",
# 	"mobile": 9835401515,
# 	"dob" : 1997,
# 	"nameList" : {"test","hello","test"}
# }

# print(mydict)

# nestedDict = {
# 	"parul" : {
# 				"name": "sharvan",
# 				"email": "s@gmail.com",
# 				"mobile": 9835401515,
# 				"dob" : 1997,
# 				},
# 	"sigma" : {
# 	"name": "sharvan",
# 				"email": "s@gmail.com",
# 				"mobile": 9835401515,
# 				"dob" : 1997,
# 	},
# 	"ntc" : {
# 	"name": "sharvan",
# 				"email": "s@gmail.com",
# 				"mobile": 9835401515,
# 				"dob" : 1997,
# 	},
# 	"bits" : {
# 	"name": "sharvan",
# 				"email": "s@gmail.com",
# 				"mobile": 9835401515,
# 				"dob" : 1997,
# 	},
# }

# print(nestedDict)

#mydict['address'] = "oproad"

# mydict.clear()

# del mydict

# print(mydict)

# mydict.popitem()
# mydict.popitem()
# mydict.popitem()

# print(mydict)

# mydict.pop("address")

# print(mydict)

# mydict.update({"address": "gotri"})

# print(mydict)


# for x,y in mydict.items():
# 	print(x,y)

# print(mydict.get("address"))

# print(mydict.keys())
# print(mydict.values())

# print(mydict.items())


# print(mydict['name'])

# mydict['address'] = "oproad"

# print(mydict)

# print(len(mydict))

# print(mydict)

# print(type(mydict))

# newDict = dict(({"name": "sharvan","email": "s@gmail.com","mobile": 9835401515,"dob" : 1997}))

# print(newDict)