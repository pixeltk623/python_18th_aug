# import example

# example.greeting("Jonathan")


# a = example.person1["age"]
# print(a)


import example as ex

a = ex.person1["age"]
print(a)


import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)


from mymodule import person1

print (person1["age"])

