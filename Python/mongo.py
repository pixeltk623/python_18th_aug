import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")

#conn = pymongo.MongoClient("mongodb+srv://sharvan:sharvan@cluster0.wkm7v.mongodb.net/sharvan?retryWrites=true&w=majority")

database = conn["python_18th_aug"]

collection = database["users"]


#data = {"name" : "Sharvan", "email" : "s@gmail.com", "mobile": 9835401515}

#data = {"_id": 2, "name" : "Sharvan", "email" : "s@gmail.com", "mobile": 9835401515}


# data = {"name" : "Sharvan", "email" : "s@gmail.com", "mobile": 9835401515}

# result = collection.insert_one(data)

# print(result.inserted_id)


# data = [
# 		{"name" : "Sharvan", "email" : "s@gmail.com", "mobile": 9835401515},
# 		{"name" : "Sharvan", "email" : "s@gmail.com", "mobile": 9835401515},
# 		{"name" : "Sharvan", "email" : "s@gmail.com", "mobile": 9835401515},
# 		{"name" : "Sharvan", "email" : "s@gmail.com", "mobile": 9835401515}
# 	]

# result = collection.insert_many(data)

# print(result.inserted_ids)

# result = collection.find_one()

# result = collection.find()


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


# collection.insert_many(mylist)

# query = {"name":"Akshat"}



# for x in collection.find(query):
# 	print(x)
# query = {"name": {"$gt": "S"}}

# for x in collection.find(query):
# 	print(x)

# query = {"name": {"$regex": "S"}}

# for x in collection.find(query):
# 	print(x)

# for x in collection.find().sort():
# 	print(x)

# for x in result:
# 	if x['_id']==3 or x['_id']==4:
# 		continue
# 	print(x)

# for x in collection.find({},{ "_id": 0, "name": 1, "email" : 1 }):
# 	print(x)

# print(result)

# print(conn)

# print(conn.list_database_names())

# print(database.list_collection_names())

# # if "admin" in conn.list_database_names():
# # 	print("Yes")

# if "customers" in  database.list_collection_names():
# 	print("Yes")


# for x in collection.find().sort('name',-1):
# 	print(x)


# query = {"name": 'SK'}

# result = collection.delete_many(query)
# print(result.deleted_count)

# totalDelete = 0
# for x in range(4,7):
# 	query = {"_id": x}
# 	result = collection.delete_one(query)
# 	totalDelete += result.deleted_count # totalDelete = totalDelete + deleted_count
# 	#print(result.deleted_count)


# print(totalDelete)

# result = collection.delete_many({})

# print(result.deleted_count)


# result = collection.drop()

# print(result)

# fetchDataQuery = {"_id": 1}

# newDataQuery = {"$set": { "name": "Shasrvan" }}

# result = collection.update_one(fetchDataQuery, newDataQuery)

# print(result.modified_count)

# totalmodified_count = 0
# for x in range(1,15):
# 	fetchDataQuery = {"_id": x}
# 	newDataQuery = {"$set": { "name": "ABC"+str(x) }}
# 	result = collection.update_one(fetchDataQuery, newDataQuery)
# 	totalmodified_count += result.modified_count; # totalmodified_count + x


# print(totalmodified_count)
# totalmodified_count = 0
# for x in range(1,15):
# 	totalmodified_count = totalmodified_count + 1; # 0 + 1 // 1  + 

# print(totalmodified_count)

# fetchDataQuery = {"name": "ABC1"}

# newDataQuery = {"$set": { "name": "Shasrvan" }}

# result = collection.update_many(fetchDataQuery, newDataQuery)

# print(result.modified_count)

# result = collection.find().limit(10)

# for x in result:
# 	print(x)