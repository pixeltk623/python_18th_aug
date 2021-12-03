# List Of Important Function

# list_database_names()
# list_collection_names()
# insert_one()
# 	#inserted_id
# insert_many()
# find_one()
# find() 
# sort()
# delete_one()
# delete_many()
# 	#deleted_count
# drop()
# update_one()
# update_many()
# 	#modified_count
# limit()


# MongoDB
# MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.


# You can download a free MongoDB database at https://www.mongodb.com.

# Or get started right away with a MongoDB cloud service at https://www.mongodb.com/cloud/atlas.

# PyMongo
# Python needs a MongoDB driver to access the MongoDB database.

# In this tutorial we will use the MongoDB driver "PyMongo".

# We recommend that you use PIP to install "PyMongo".

# PIP is most likely already installed in your Python environment.

# Navigate your command line to the location of PIP, and type the following:

# Download and install "PyMongo":

# python -m pip install pymongo

import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["mydatabase"]

# print(myclient.list_database_names())


# mycol = mydb["customers"]


# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#   print("The database exists.")


# collist = mydb.list_collection_names()
# if "customers" in collist:
#   print("The collection exists.")


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase4665"]
# mycol = mydb["customers4665"]

# print(mydb.list_collection_names())


# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)


# # x = mycol.insert_many(mylist)



# print(x.inserted_id)

# x = mycol.find_one()

# print(x)

# for x in mycol.find():
#   print(x)




#myclient = pymongo.MongoClient("mongodb+srv://sharvan:sharvan@cluster0.wkm7v.mongodb.net/sharvan?retryWrites=true&w=majority")

myclient = pymongo.MongoClient("mongodb://localhost:27017/");

mydb = myclient["python_nov"]

# dblist = myclient.list_database_names()

mycol = mydb["customers"]

# mydict = { "name": "John", "email" : "s@gmail.com",  "address": "Highway 37" }

# x = mycol.insert_one(mydict)

# print(x.inserted_id)
# print(x)

# collist = mydb.list_collection_names()

# print(collist)


#insertMany

# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)


# Insert Multiple Documents, with Specified IDs
# If you do not want MongoDB to assign unique ids for you document, you can specify the _id field when you insert the document(s).

# Remember that the values has to be unique. Two documents cannot have the same _id.


# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# In MongoDB we use the find and findOne methods to find data in a collection.

# Just like the SELECT statement is used to find data in a table in a MySQL database.

# Find One
# To select data from a collection in MongoDB, we can use the find_one() method.

# The find_one() method returns the first occurrence in the selection.

# x= mycol.find_one()

# print(x)


# Find All
# To select data from a table in MongoDB, we can also use the find() method.

# The find() method returns all occurrences in the selection.

# The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.

# No parameters in the find() method gives you the same result as SELECT * in MySQL.


# x= mycol.find()

# for y in x:
# 	print(y)


# Return Only Some Fields
# The second parameter of the find() method is an object describing which fields to include in the result.

# This parameter is optional, and if omitted, all fields will be included in the result.


# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#   print(x)


# for x in mycol.find({},{ "address": 0 }):
#   print(x)

# MongoDB Query


# Filter the Result
# When finding documents in a collection, you can filter the result by using a query object.

# The first argument of the find() method is a query object, and is used to limit the search.

# myquery = { "address": "Highway 37" }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)



# Advanced Query
# To make advanced queries you can use modifiers as values in the query object.

# E.g. to find the documents where the "address" field starts with the letter "S" or higher
#  (alphabetically), use the greater than modifier: {"$gt": "S"}:

# myquery = { "address": { "$gt": "S" } }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)


# Filter With Regular Expressions
# You can also use regular expressions as a modifier.
# To find only the documents where the "address" field starts
# with the letter "S", use the regular expression {"$regex": "^S"}:

# myquery = { "address": { "$regex": "^S" } }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)


# Sort the Result
# Use the sort() method to sort the result in ascending or descending order.

# The sort() method takes one parameter for "fieldname" and one parameter for "direction"
# (ascending is the default direction).

# mydoc = mycol.find().sort("name")

# for x in mydoc:
#   print(x)

# sort("name", 1) #ascending
# sort("name", -1) #descending

# mydoc = mycol.find().sort("name", -1)

# for x in mydoc:
#   print(x)

# Delete Document
# To delete one document, we use the delete_one() method.

# The first parameter of the delete_one() method is a query object defining
# which document to delete.

# Note: If the query finds more than one document, only the first occurrence is deleted.

# myquery = { "address": "Mountain 21" }

# mycol.delete_one(myquery)


# Delete Many Documents
# To delete more than one document, use the delete_many() method.

# The first parameter of the delete_many() method is a query object
#  defining which documents to delete.

# myquery = { "address": {"$regex": "^S"} }

# x = mycol.delete_many(myquery)

# print(x.deleted_count, " documents deleted.")


#Delete All Documents in a Collection


# x = mycol.delete_many({})

# print(x.deleted_count, " documents deleted.")



# Delete Collection
# You can delete a table, or collection as it is called in MongoDB, by using the drop() method.

# mycol.drop()


# Update Collection
# You can update a record, or document as it is called in MongoDB, by using the update_one() method.

# The first parameter of the update_one() method is a query object defining which document to update.

# Note: If the query finds more than one record, only the first occurrence is updated.


# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }

# mycol.update_one(myquery, newvalues)

# #print "customers" after the update:
# for x in mycol.find():
#   print(x)


# x = mycol.update_many(myquery, newvalues)

# print(x.modified_count, "documents updated.")


# Limit the Result
# To limit the result in MongoDB, we use the limit() method.

# The limit() method takes one parameter, a number defining how many documents to return.

# Consider you have a "customers" collection:


# myresult = mycol.find().limit(5)

# #print the result:
# for x in myresult:
#   print(x)