import mysql.connector

# mydb = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password=""
# )


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="php_03030"
)


cursorNew = mydb.cursor() 

query = "CREATE TABLE employee ( id int PRIMARY KEY AUTO_INCREMENT, name varchar(255), email varchar(255) )"

cursorNew.execute(query)

# print(cursorNew)