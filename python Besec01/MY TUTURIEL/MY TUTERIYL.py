#import pywhatkit
"""
Python:
    variable 
    conditions
    loops
    class

Variable:
    Premitive
        character
        string
        interger
        flaot
        boolean
        complex
    Non-premitive:
        - List
        - tuple
        - set
        - dictionary

Inbuilt functions:
    - print()
    - type()




"""
# varible declaration
# variableName = someValue
# name = "Saurabh"
# print(name)
# print(type(name))
# name = "Jay"
# print(type(name))
# print(name)
# name = 2.3
# print(type(name))
# print(name)
# name = True  # Boolean has only two value i.e. True,  False those are also considered as 1, 0 respectively
# print(type(name))
# print(name)
# name = "Y"
# print(type(name))
# print(name)
# name = 3 + 7j  # complex number (real number + imaginary number)
# print(type(name))
# print(name)

# String
# slicing:
# forward slicing
# backword slicing

# studentName = "Jay Jadhav"
# studentName1 = "VaibhaV Arde"
# firstName = studentName[0:3]
# print(firstName)
# lastName = studentName[4::1]
# print(lastName)
# nameLength = len(studentName)
# print(nameLength)
# certerChar = studentName1[int(len(studentName1) / 2)]
# print(studentName1[int(len(studentName1) / 2)])
# print(certerChar)
# print(7 / 2)
# print(int(4 / 2))
# slicing:
# variableName[startPosition:endPosition:jump]
# endPosition: bydefault given endPosition is excluded while slicing
# jump: bydefault jump is 1

# Reverese
# randomString = "wertyuisdfghjkvbnm"
# print(randomString[::-1])
# print(randomString[::-2])

# # typecasting
# num = 6789
# print(str(num))
# print(type(str(num)))

# studentName1 = "VaibhaV Arde"
# print(studentName1.upper())
# print((studentName1.upper()).isupper())
# print(studentName1.lower())
# print((studentName1.lower()).isupper())

# print(studentName1.count("a"))  # 2
# print(studentName1.count("A"))  # 1
# print(studentName1.title())  # Vaibhav Arde
# print(studentName1.capitalize())  # Vaibhav arde

# ++++++++++++++++++++++++++++++++++++++++++
# list
# list has indices, index starts from 0
# list can store any type of varible
# list is mutable


# names = ["Jay", "Saurabh", "VaibhaV", "Sangram", "Mangesh"]
# print(names[1])
# print(len(names))
# print(len(names[1]))
# print(names[3][3])

# names1 = ["Jay", "Saurabh", "VaibhaV", "Sangram", "Mangesh"]
# names1[0] = "Sakshi"
# print(names1)
# names1.append("Vaishnavi")
# print(names1)
# names1.insert(0, "Jay")
# print(names1)
# names1.insert(3, "Sarvjeet")
# print(names1)
# names1.remove("Saurabh")
# print(names1)
# names1.pop()
# print(names1)

# randomList = [
#     1,
#     345,
#     9.3,
#     "d",
#     "VaibhaV",
#     2 + 5j,
#     True,
#     {"name": "VaibhaV"},
#     {"number": 1234567890},
#     names1,
# ]

# # print(randomList)
# print(randomList[-1][-1][3])
# ++++++++++++++++++++++++++++++++++++++++++++++

# tuple
# Tuple is immutable
# Tuple has indices, index starts from 0
# Tuple can store any type of varible
# randomTuple = (
#     1,
#     345,
#     9.3,
#     "d",
#     "VaibhaV",
#     2 + 5j,
#     True,
#     {"name": "VaibhaV"},
#     {"number": 1234567890},
#     [3, "t", 6, 7, "Text"],
#     9.3,
# )

# print(randomTuple.index(9.3))
# print(randomTuple.count(9.3))

# ++++++++++++++++++++++++++++++++++++++
# Set:
# Set is immutable
# Set has hasing
# Set has no duplicates
# Set has no sequence/order
# So sets are mutable but can't contain mutable items, because set internally uses hashtable to store its elements so for that set elements need to be hashable. But mutable elements like list are not hashable.
# randomSet = {
#     1,
#     345,
#     9.3,
#     "d",
#     "VaibhaV",
#     2 + 5j,
#     True,
#     9.3,
# }
# print(type(randomSet))
# randomSet.add(2)
# randomSet.add(2)  # set store unique values hence this second 2 is not added
# print(randomSet)
# print(randomSet.pop())
# print(randomSet)
# print(randomSet.pop())
# randomSet.remove(2)
# print(randomSet)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++

# Dictionary:
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’.
# Dictionary holds pairs of values, one being the Key and the other corresponding pair element being its Key:value.
# Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.

# Dict1 = {1: "Geeks", 2: "For", 3: "Geeks"}
# print(Dict1)

# # Creating a Nested Dictionary
# # as shown in the below image
# Dict2 = {1: "Geeks", "me": "For", 3: {"A": "Welcome", "B": "To", "C": "Geeks"}}
# print(Dict2)

# print(Dict2["me"])
# print(Dict2[3]["C"])
# print(Dict2[3]["A"])
# Dict2.update({4: "Test"})
# print(Dict2)
# Dict2[3]["B"] = "Two"
# print(Dict2)

# print(Dict2.pop("me"))
# print(Dict2)
# print(Dict2.popitem())
# print(Dict2)

# Dict1 = {1: "Geeks", "me": "For", 3: {"A": "Welcome", "B": "To", "C": "Geeks"}}
# print(Dict1)
# print(Dict1.popitem())
# print(Dict1)

# Dict1.update({"me": "For"})
# print(Dict1)
# Dict1.update({"me1": "For"})
# print(Dict1)
# Dict1.update({"me0": "For"})
# print(Dict1)

# print(Dict1.popitem())
# print(Dict1)




