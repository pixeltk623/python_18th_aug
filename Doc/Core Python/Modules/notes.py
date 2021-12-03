# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

# Create a Module
# To create a module just save the code you want in a file with the file extension .py:



What is PIP?
PIP is a package manager for Python packages, or modules if you like.


What is a Package?
A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.

Check if PIP is Installed
Navigate your command line to the location of Python's script directory, and type the following:

pip install pip



pip --version



pip install camelcase


import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))



Find Packages
Find more packages at https://pypi.org/.

Remove a Package
Use the uninstall command to remove a package:



pip uninstall camelcase



pip list

import math


x = math.sqrt(64)

print(x)



x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


x = math.pi

print(x)