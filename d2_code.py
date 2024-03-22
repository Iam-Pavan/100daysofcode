#python primitive data types
#strings
print("pavan"[4])

print("123"+"345")
# integer
print(123+456)
#121_234_456
# float 3.25448

# boolean true or false
print("***type error type checking type conversion")
# num_char = len(input("whate is your name"))
# print("your name has"+num_char+"characters")
# erro
# rTraceback (most recent call last):
#   File "/home/pavan/100daysofcode/100daysofcode/d2_code.py", line 14, in <module>
#     print("your name has"+num_char+"characters")
#           ~~~~~~~~~~~~~~~^~~~~~~~~
# TypeError: can only concatenate str (not "int") to str

new_char = len(input("what is your name: \n"))
#converted int into str
new_num_char = str(new_char)
print("your name has "+new_num_char+" characters")

a = str(123)
print(type(a))
print(40+float("70"))
#float add 40+70
print(str(5)+str(5))

print("#interactive coding exercise\n")
two_digit_number = input("enter number: \n")
first_digi = int(two_digit_number[0])
second_digit  = int(two_digit_number[1])

# add two integers togather
two_digit_number = first_digi + second_digit
print(two_digit_number)

print("**mathematical operators in python")
# pemdas
# ()
# **
# *
# /
# -
# +
print(3*3+3/3-3)
# 3*3 9, 3/3 1.0, 9+1.0, -3
print(3*(3+3)/3-3)
#3+3 6, 3*6 18, 18/3 3.0,
print("**[Interactive Coding Exercise] BMI Calculator\n")
# 1st input enter height in meter e.g: 1.65
height = input("enter height: ")
# 2nd input enter weight in kilograms e.g: 72
weight = input("enter weight: ")

height_as_float = float(height)
weight_as_int = int(weight)

bmi = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi)
print(bmi,"\n")

print("***Number Manipulation and F Strings in Python")
# print(8/3)
print(int(8/3))
#round  8/3 n_digits
print(round(8/3,2))
result = 4/2
result /=2
print(result)

score = 0
score += 1
print(score)

print("the score is: "+str(score))
# f-string
print(f"the score is {score}, the result is {result}")

print("**[Interactive Coding Exercise] life in weeks\n")

age = input("age: ")
# your code below this line
years = 90 - int(age)
weeks = years * 52
print(weeks)
print(f"you have {weeks} left.")

