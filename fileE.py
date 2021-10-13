# open() function
# “ r “, for reading.
# “ w “, for writing.
# “ a “, for appending.
# “ r+ “, for both reading and writing


# files = open("test.txt", 'r')

# allFiles = files.read()


# allFiles = files.read(10)

#print(allFiles)

# print(files.readline())
# print(files.readline())
# print(files.readline())
# print(files.readline())

# files = open("test.txt", 'w')

# # print(files)

# files.write("This is New Para")
# files.write("This is New Para")
# files.write("This is New Para")


# files = open("test.txt", "r")

# print(files.read())


# files = open("test.txt", "a")

# files.write("This is New Para")

# f = open("test.txt", "r")

# print(f.read())

# f.close()



# print(files)

#Python code to illustrate split() function
# with open("test.txt", "r") as file:
# 	data = file.readlines()
# 	#print(data)
# 	for line in data:
# 		word = line.split()
# 		print (word)


# import os

# if os.path.exists("remove.txt"):
# 	os.remove("remove.txt")
# else:
# 	print("Nahi Hai")

# os.rmdir("dummy")
# 6
# 66
# 666
# 6+66+66

# number = int(input("Enter Your Number: - "))

# n1 = int( "%s" % number )
# n2 = int( "%s%s" % (number,number) )
# n3 = int( "%s%s%s" % (number,number,number) )

# # print(n1,n2,n3)

# # print(type(n1))

# print(n1+n2+n3)


# Python program to illustrate
# Append vs write mode
# file1 = open("myfile.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London"]
# file1.writelines(L)
# file1.close()

# file1 = open("myfile.txt", "r")

# print(file1.read())


# file1 = open("myfile.txt", "a") # append mode
# file1.write("Today \n")
# file1.close()

# file1 = open("myfile1.txt", "a") # append mode
# file1.write("Today \n")
# file1.close()

# file1 = open("myfile.txt", "r")
# print("Output of Readlines after appending")
# print(file1.read())
# print()
# file1.close()



