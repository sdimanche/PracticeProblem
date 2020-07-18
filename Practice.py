# # #Example of printing
print("Hello, World!")
# # Blank lines are ignored!
# # # You can use an empty print statement to create a space between your lines
# print()
# print("1 2 3")
# # print()

# # #Line continuation
# sum = 1 \
#      + 2 
# print()


# #Example of Arithmetic Operators
# # Addition, subtraction
# print(5 + 5)
# print(5 - 5)
# #Multiplication, division, modulo, and exponent
# print(3 * 5)
# print(10 / 2)
# #Note, when using /, your result becomes a float 
# print(18 % 7)
# print(4 ** 2)
# print()



# # # INTEGERS
# # #In Python, there is effectively no limit to how long an integer value can be. Of course, it is constrained by the amount of memory your system has, as are all things, but beyond that an integer can be as long as you need it to be:
# print(123123123123123123123123123123123123123123123123 + 1)
# print()

# # # The float type in Python designates a floating-point number. Float values are specified with a decimal point.
# print(4.2)
# print(".2")
# print()

# # # Strings
# # #Strings are sequences of character data. The string type in Python is called str.
# # #Character data stores strings of letters, numbers, and symbols
# # #String literals may be delimited using either single or double quotes. All the characters between the opening delimiter and matching closing delimiter are part of the string:
# print("I am a string.")
# print("I am"+" a string!!!")
# print('I am too.')

# # #Rule: 
# # #In one line only a single executable statement should be written and the line change acts as command terminator in python.
# # #To write two separate executable statements in a single line, you should use a semicolon ; to separate the commands. For example:
# print()
# print("How are you?"); print("I'm good")

# # #Boolean
# # #Python provides a Boolean data type. Objects of Boolean type may have one of two values, True or False
# print()
# print(type(True))
# print(type(False))
# print()


# # #
# # #
# # # Using the type() function to identify data type
# x = 10
# print(type(x))
# z = 10.55
# print(type(z))
# # y = 1 + 2j
# # print(type(y))
# a = True 
# print(type(a))
# b = "Hi"
# print(type(b))
# print()

# # #How to do casting:
# # #For integers
# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int(3.4) # z will be 3
# print(x)
# print(y)
# print(z)
# print()

# # #For floats
# a = float(1)     # x will be 1.0
# print(a)
# b = float(2.8)   # y will be 2.8
# print(b)
# c = float(3)   # z will be 3.0
# print(c)
# d = float("4.2") # w will be 4.2
# print(d)
# print()

# # #For strings
# l = str("s1") # x will be 's1'
# print(l)
# k = str(2)    # y will be '2'
# print(k)
# j = str(3.0)  # z will be '3.0'
# print(j)
# print()



# # # #Reproducibility 
# height = 1.79
# weight = 68.7
# bmi = weight / height ** 2
# print(bmi)
# print()

# # # # #Error example!!!!
# # # #
# print("My BMI: " + str(bmi))
# print()


# #if/else statements 
# number = 10
# if number % 2 == 0: #not even
#   print(number)
# else:
#   print("Even number")
# print()

# # #Additional Example
# a = 100
# b = 100
# if a < b:
#   print("a is not greater than b")
# elif a > b:
#   print("a is greater than b")
# else:
#   print("a and b are equal")

# name = input("What is your name?")
# print(name)


# # # Let's Practice!
# if 5 > 2:
#  print("Five is greater than two!")

# if 5 > 2:
#  print("Five is greater than two!") 
#  print("Five is greater than two!")

# #Python will give you an error if you skip the indentation:

# #You have to use the same number of spaces in the same block of code, otherwise Python will give you an error