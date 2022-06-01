#
#                                           Output & Printing
# print() is how to output the code in console ex: print("hello") or print(499)
#
#                                       DATA TYPES:
#                                     Text or numbers
#
# Text Type(STRING): are string within single or double quotes. 'str' or "str" ex: "I am human" or 'I am human'
#
# Bool: Boolean meaning true or false.

# Number Types(): Integer(Int) or Float Point Number(Float)
#
# int: whole number positive or negative without decimal. ex: (75), (49), (-100), (1500), (0)
#
# float: is a precision number usually containing 1 or more decimals. ex: (3.5), (-75.33), (0.444)
#
# print (-34) #---> INT
# print ("Your total is 454.11") #--->STRING
# print(0.74) #---> FLOAT


#                            Arithmetic Operators:
#               used with numeric values for mathematical operations.
# Can do (+,
# - = subtraction
# + = addition
# / = division
# * = multiplication
# ** =  exponents
# // = whole number division
# ex:
# print(6 + 4)
# # should =10
# y = 4
# x = 6
# results = y + x
# print(results)
# # should =10
#
# print(15 - 3)
# # should = 12
# y = 3
# x = 15
# results2 = y - x
# print(results2)
# # should = -12
#
# print(2 * 50)
# # should =100
# y = 50
# x = 2
# results3 = y * x
# print(results3)
# # should =100
#
# print(80 / 2)
# # should =40
# y = 80
# x = 2
# results4 = y / x
# print(results4)
# should =40


#                                Python conditional Operators
#                           WILL ONLY RETURN A BOOL Data type

# ==  means equal
# ex:
#  a = 20
#  x = 20
#  print(a == x)
#  returns true 20 & 20 or a & x are equivalent

# != : not equal
# ex:
# y = 13
# z = 74
# print(y != z) returns true
# returns true 74 & 13 aren't equals

# > : greater than
# ex:
# k = 10
# n = .456
# print(n > k)
# returns false because .456 is not greater than 10

# => : greater than or equal to
# ex:
# k = 10
# n = .456
# print(n > k)
# returns true because .456 is less than 10

#                                          Chained conditionals
#  and / or /  not  are used to chain larger conditions

#                                           if/else & elif

# there can only be 1 if & 1 else statement. Else must always come after an if statement
# if else is very black & white for one to be true the other need to be false

# x = input("Name: ")

# if x == "zay":
#     print('You the goat')
# else:
#     print("You aren't a goat")

# elif can only be used after and if and before else. You can have a multitude of elif statements
# x = input("Name: ")
#
# if x == "zay":
#     print('You the goat')
#
# else:
#     print("You aren't a goat")

#                                           String Method
# .lower, .upper, .capitalize, .count

# name = "zay"
# print(name.upper())
# # should return ZAY
# name1 = "BIG ZAY"
# print(name1.lower())
# # should return big zay
# state = "georgia"
# print(state.capitalize())
# # should return Georgia
# state2 = "Mississippi"
# print(state2.count('s'))
# # should return 4


#                                         Sting Concatenation
#       is fancy for adding strings together. Using the + or f {} is how to connect a series of strings.

# x = "yo"
# y = 3
# print(y * x)

# #ex: "12 roses are" + str(24) + " in usd."
# print( "12 roses are " + str(24) + " in usd.")
# # should return --> 12 roses are 24 in usd.
# # a cleaner way of doing it could be
# print(f"12 roses are {24} in usd.")
# # should return --> 12 roses are 24 in usd.
# print(f"12 roses are {2 * 12} in usd.")
# Python 3.6 or higher has access to this new syntax


#                                            Variables:
#                     storing values that will repeat throughout the code.
#
# In variable name underscores are allowed. Cant' start with a number

# print(f"12 roses are {2 * 12} in usd.")
# print(f"7 roses are {2 * 7} in usd.")
# print(f"30 roses are {2 * 30} in usd.")
# print(f"1000 roses are {2 * 1000} in usd.")

# Above are different calculations per quantity of roses in usd
# What a variable will do stop the repetitive code

# price_of_roses = 2
# Here the variable is price_of_roses & 2 is the value

# print(f"12 roses are {price_of_roses * 12} in usd.")
# print(f"7 roses are {price_of_roses * 7} in usd.")
# print(f"30 roses are {price_of_roses * 30} in usd.")
# print(f"1000 roses are {price_of_roses * 1000} in usd.")
# if you run the print command it should return the sum of the amount of roses times out variables value of 2


#                                        Functions
#            are blocks of code that that can be used to avoid repeating logic

# are describe by the def tag ex:
# naming functions are similar to variables descriptive and unique
# functions can many lines of code

# create a functions below using def tab
# def quantity_of_roses():
# print(f"12 roses are {price_of_roses * 12} in usd.")
# print ("Are you a loyalty member")

# Calling/using/executing a function is now made simple using the name given after the def tag
#  quantity_of_roses()


#                                         Parameters
#       are information passed into functions as parameters, Parameters are also known as arguments(args)

# def quantity_of_roses():
# print(f"12 roses are {price_of_roses * 12} in usd.")
# print ("Are you a loyalty member")

# Our current function is locked into the value of 12 for number of rose
# To have cleaner looking code you'd want to define your input parameters within the function


#  price_of_roses = 2  # variable
#  legal_tender = "usd"    # variable


# def quantity_of_roses(num_of_rose, custom_message):
#     print(f"{num_of_rose} roses are {price_of_roses * num_of_rose} in usd.")
#     print(custom_message)


#  quantity_of_roses(44, "Is this a pre-order")
#  quantity_of_roses(2, "We currently have a 1/2 dozen deal?")
#  quantity_of_roses(100, "Who's so lucky")


#                                           Variable Scope
#                               Defines the accessibility of variables

#    Global Scope Variables : means the variables outside of a function  can be used elsewhere throughout a
# project.
#
# In our example legal_tender & price_of_rose are both considered variables on a global scope. can be used
# elsewhere throughout a project


# price_of_roses = 2 # variable
# legal_tender = "usd"  # variable
#
# def quantity_of_roses(num_of_rose, custom_message):
#     print(f"{num_of_rose} roses are {price_of_roses * num_of_rose} in {legal_tender}.")
#     print(custom_message)

#      Local Scope Variable: means that variables created inside the function can only be used with that function

# In our example num_of_rose & custom_message are both considered variables on a on Local scope. THEY CAN NOT BE USED
# used elsewhere THEY EXCLUSIVELY BELONG TO quantity_of_roses function. Not suggested but private/local scope
# variables can share a name and not effect another as long as the function name is unique

# price_of_roses = 2  ---> variable  Global outside
# legal_tender = "usd"  ---> variable  Global outside


#                        belongs to function
# def quantity_of_roses(num_of_rose, custom_message):
#     print(f"{num_of_rose} roses are {price_of_roses * num_of_rose} in {legal_tender}.")
#     print(custom_message)
#
#
# def scope_check(num_of_rose):
#     print(legal_tender) ---> variable Global
#     print(num_of_rose) ---->variable owned buy scope_check
#
#
# scope_check(3)

#            !!!!!come back                         USER INPUT
#           User Input is a function built into python by using input().Giving users the ability to make input
#
# input must be a string. input("age: ")
# Name = input("Name: ")
# Age = input("Age: ")
#
# input("Please pick your the amount of roses you'd like!")
#  to gain cleaner look attach  \n at the end of your input string to allow next line response
# input("Please pick your the amount of roses you'd like!\n")
#  input can also be used as a variable
#
# customer_response = input("Please pick your the amount of roses you'd like!\n")
#
# print(customer_response)

#                                         List
#               is an ordered collection that stores different elements commonly defined with [...] brackets

# x = ["red", True, "flew", 2]
# print(x)
# # list functions
# #   len() = length:  check the actual length od the
# x = ["red", True, "flew", 2]
# print(len(x))

# #  .append  adds elements to the end of the list.
# x = ["red", True, "flew", 2]
# x.append('cat')
# print(x)

# #  .extend  adds a list of elements to the end of the list.
# x = ["red", True, "flew", 2]
# x.extend(['cat', "car", 5, 7, 5, 4, 3, 3, 3])
# print(x)

# #   pop() will remove and last element of the list if unspecified
# x = ["red", True, "flew", 2]
# print(x.pop())

# # to remove a specific element with the pop command find the index of the element by getting its place in the list
# # and subtract 1
# x = ["red", True, "flew", 2]
# print(x.pop())

# # to remove 2 using pop() function  which is also our 4th element of the list. Granted we see 4 elements in the list
# # but the first position is actually 0 and the rest follows in a sequential order.
# # So 2 is visibly sitting 4th on the list but its index is actually 3 because the index starts at 0
# x = ["red", True, "flew", 2]
# print(x.pop(3))

# to change a value of an element withing the list you can identify the elements index and then change its value so
# basically we are going to change flew into ran
# x = ["red", True, "flew", 2]
# x[2] = "ran"
# print(x)

#                                                Tuples:
#               are emutable list meaning they can't be changed and are used with () vs []

#                                              For loops
#                               allow iteration a set number of times
# for i in range(5):
#     print(1)


#                                              While loops
#                      can run an infinite amount of times because it is based off a condition
#
# i = 4
# while i <= 11:
#     print("run")

# while loop with break statement
#
# i = 0
# while True:
#     print("run")
#     i -= 1
#     while True:
#         if i == 10:
#             break   # break stops the while loop

#                                                    sliced Operator
#                                    allows you to take any part of a collection ie. string/list/tuple
x = [3, 4, 5, 6, 22, 11, 56, 65]
y = ["Yo, AYO, hey, hi"]
s = "Heya"

# sliced = x[start:stop:step]
sliced = x[1:6:7]
