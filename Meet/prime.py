count=0
userInput=int(input("enter the number"))
if userInput<1:
	print("invalid number")
else:
	if userInput==1:
		print("1 is special number")
	else:
		for x in range(1,userInput+1):
			if userInput%x==0:
				count=count+1
		if count==2:
			print(userInput,"number is prime")
		else:
			print(userInput,"number is not prime")

