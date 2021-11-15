from tkinter import *
import mysql.connector
import tkinter.messagebox as m


def databaseConnection():
	conn = mysql.connector.connect(
		 host="localhost",
		 user="root",
		 password="",
		 database="Python_18_aug"
		)

	return conn



def saveData():

	nameD = nameE.get()
	emailD = emailE.get()
	mobileD = MobileE.get()

	if nameD=='':
		m.showinfo("Message", "Name can Not be blank")
	if emailD=='':
		m.showinfo("Message", "Email can Not be blank")
	if mobileD=='':
		m.showinfo("Message", "Mobile can Not be blank")


	if nameD !='' and emailD !='' and mobileD !='':

		db = databaseConnection()
		cursor = db.cursor()

		query = "INSERT INTO `users`(`name`, `email`, `mobile`) VALUES ('"+nameD+"','"+emailD+"','"+mobileD+"')";

		cursor.execute(query)
		db.commit()

		m.showinfo("Message", "All Ok")
	else:
		m.showinfo("Message", "Error")

interFace = Tk()
interFace.geometry("500x500")
interFace.title("CRUD")
interFace.configure(bg="lightblue")


v = StringVar(interFace, "1")
 
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
        "RadioButton 2" : "2",
        "RadioButton 3" : "3",
        "RadioButton 4" : "4",
        "RadioButton 5" : "5"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(interFace, text = text, variable = v,
        value = value).pack(side = TOP, ipady = 5)

        

name = Label(interFace, text="Enter Your Name")
name.place(x=50, y = 40)

email = Label(interFace, text = "Enter Your Email")
email.place(x=50, y= 90)

mobile = Label(interFace, text = "Enter Your Mobile")
mobile.place(x=50, y=140)


# city = Label(interFace, text = "City")
# city.place(x=50, y=190)

nameE = Entry()
nameE.place(x=180, y = 40)

emailE = Entry()
emailE.place(x=180, y = 90)

MobileE = Entry()
MobileE.place(x=180, y = 140)


button = Button(interFace, text="Save", bg="White", command=saveData)
button.place(x=110, y=200, width=100)





mainloop()