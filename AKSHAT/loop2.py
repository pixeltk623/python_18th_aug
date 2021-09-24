# print("check for prime")
# count=0
# userInput=int(input("enter the number"))
# if userInput<1:
# 	print("invalid number")
# else:
# 	if userInput==1:
# 		print("1 is special number")
# 	else:
# 		for x in range(1,userInput+1):
# 			# print(x)
# 			if userInput%x==0:
# 				count=count+1
# 		if count==2:
# 			print(userInput,"number is prime")
# 		else:
# 			print(userInput,"number is not prime")



print("prime between 1-100")
for x in range(1,101):
	count=0
	for y in range(1,x+1):
		if x%y==0:
			count=count+1
	if count==2:
		print(x,"prime")
	else:
		print(x,"not prime")


			
		