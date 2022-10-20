#To run Python script in terminal: 
# python <scriptname.py> #

### Day 1 ###


## Basics ##

# len() #
print(len("Hello"))
#Printing the length of the string

# \n #
print("meow\nmeow")
#This is a line break,and will move the next word in the string down one in the output

# input() #
print('input("Is this a input example? " + "Yes")')
#This will prompt this user to provide an input
#It is wrapped in print() as to not interrupt the flow of the output


### Day 2 ###


# [0], [1], ect #
print("meow"[0])
#This is called "Subscript", and will index the entered vaule within "[]", this example the value of 0 is index. 
#Giving us "m" from the string, The vaule of 1 would give us "e", so on and so forth.
#Spaces also are counted (indexed)

## Data Types ##

# Integer #
print(123)
#Any whole number

# Floats #
print(2.53)
#Floats are any decimal

# Boolean #
print("True -or- False")
#Ture or False statment

## Convertions ##

# Type() #
print(type(1))
#Will check the data type of the vaule or variable, 
#this will output <int> for Integer

# Str() #
print(str(5))
#Converts the Integer into a String

# Int() #
print(int("346"))
#Converts the string into a Integer

# Float() #
print(float("100.75"))
#Converts the string into a floating (decimal) number

## Mathematical Operations ##

# Bacis #

# Adding "+"
# Subtracting "-"
# Multiplication "*"
# Division "/" (Division is always a float)

# Order of Operation #
# Parentheses
# Exponents
# Multiplication & Division
# Addition & Subtraction 
# Calculation are prefromed left to right
# Exmaple 3 / 3 * 3, Division is preformed first.

# Exponent #
print(2 ** 2)
# 2 to the power of 2

# Rounding #
print(round(2/3, 2))
#this will round the equation two decimal by the comma 2

# Floor Division #
print (8 // 3)
#This will product a whole number,
#cutting off everything after the decimal,
#This will also change the data type to an integer

# F string #
value = 1 
print(f"text {value}")
#This is an F string, this will allow you to,
# add an integer to a string without converting datatypes


## Day 3 ##

#Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not Equal to
# % Modulo, Divids and outputs the reminder 
meow = 1
lilkat = 2
if meow == lilkat:
    print("meow and lilkat are the same")
else:
    print("meow and lilkat are NOT the same")

#elfi#
#added condition

#Nested if/elfi/else statments

# Logical Operators #
#A and B
#C or D
#not E


# For loops #
list = [34,5345,345]

for i in list: 
    print(i)
# the for loop with iterate through the list and print each item
# within said list #

# For loop with addition #
total = 0

for i in list:
    total += i
print(total)

# can also be done with Sum()

# For loop to count number of object
x = 0
for a in list:
    x += 1
print(x)

#can also use len()

