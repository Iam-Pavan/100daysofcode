print("hello python 22/may/2024")
print("the python day_1 learning python code\n")

print("**print modifiers")
print("--------------------")
# print("she said: "hello" and then left.")
print("she said: 'hello' and then left.")
# print('she said: 'hello' and then left.')

#  File "/home/pavan/100daysofcode/100daysofcode/d1_code.py", line 20
#     print(day 1-string manipulation")
#                                    ^
# SyntaxError: unterminated string literal (detected at line 20)
print('she said: "hello" and then left')
# the \"escape\" is known to the compiler
print("alternative you can just \"escape\" the quote\n")

print("**string manipulation and code intelligence")
# \n is the new line command
print("hello world\nhello world\n")
print("--string concatenation")
print("hello"+" "+"iam"+" "+"py\n")

print("**debugging practice \n")
#1.missing double quote before the word day
# print(day 1-string manipulation")
print("day 1-string manipulation")

# 2.outer double quotes changed to single quote
# print("string concatenation is done with the "+" sign.")
print('string concatenation is done with the "+" sign ')

# 3.extra indentation removed
#  print('e.g print("hello"+"helo")')
print('e.g print("hello"+ "world")\n')

# 4.extra parentheses
#print(("hello world")
print("helo world\n")
#python the input function
print("**python the input function")
print('the input("A prompt for the user") ')
# input("what is your name?")
#input() will get user input in console
# then print() will print the word "hello" and the user input
print("hello "+ input("what is your name?")+"!")
print(len(input("what is your name?\n")))

# python variables
print("**python variables")
name = "Elite\n"
print(name)
name = input("wht is your name?\n")
print(name)

length = len(name)
print(length)

#there are two variables ,a and b
print("**switching variable")
a= input()
b= input()
#creating a third variable to help switch the variable
c = a
a = b
b = c
print("a:" +a)
print("b:"+b)
print("**variable naming")
print()




