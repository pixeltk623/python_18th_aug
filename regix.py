import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	


# re.findall()
# The re.findall() method returns a list of strings containing all matches.

# import re

# string = 'hello 12 hi 89. Howdy 34'
# pattern = '\d+'

# result = re.findall(pattern, string) 
# print(result)

# # Output: ['12', '89', '34']


# re.split()
# The re.split method splits the string where there is a match and returns
# a list of strings where the splits have occurred.


# import re

# string = 'Twelve:12 Eighty nine:89.'
# pattern = '\d+'

# result = re.split(pattern, string) 
# print(result)

# # Output: ['Twelve:', ' Eighty nine:', '.']



# import re

# string = 'Twelve:12 Eighty nine:89 Nine:9.'
# pattern = '\d+'

# # maxsplit = 1
# # split only at the first occurrence
# result = re.split(pattern, string, 1) 
# print(result)

# # Output: ['Twelve:', ' Eighty nine:89 Nine:9.']

# re.sub()
# The syntax of re.sub() is:

# re.sub(pattern, replace, string)
# The method returns a string where
# matched occurrences are replaced with the content of replace variable.


# Program to remove all whitespaces
# import re

# # multiline string
# string = 'abc 12\
# de 23 \n f45 6'

# # matches all whitespace characters
# pattern = '\s+'

# # empty string
# replace = ''

# new_string = re.sub(pattern, replace, string) 
# print(new_string)

# Output: abc12de23f456


# re.search()
# The re.search() method takes two arguments: a pattern and a string. The method looks for the first location where the RegEx pattern produces a match with the string.

# If the search is successful, re.search() returns a match object; if not, it returns None.

# match = re.search(pattern, str)


import re

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

# Output: pattern found inside the string



# import re

# string = '39801 356, 2102 1111'

# # Three digit number followed by space followed by two digit number
# pattern = '(\d{3}) (\d{2})'

# # match variable contains a Match object.
# match = re.search(pattern, string) 

# if match:
#   print(match.group())
# else:
#   print("pattern not found")

# # Output: 801 35