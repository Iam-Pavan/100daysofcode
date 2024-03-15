#python primitive data types
#strings
print("pavan"[4])

print("123"+"345")
# integer
print(123+456)
#121_234_456
# float 3.25448

# boolean true or false

# num_char = len(input("whate is your name"))
# print("your name has"+num_char+"characters")
# erro
# rTraceback (most recent call last):
#   File "/home/pavan/100daysofcode/100daysofcode/d2_code.py", line 14, in <module>
#     print("your name has"+num_char+"characters")
#           ~~~~~~~~~~~~~~~^~~~~~~~~
# TypeError: can only concatenate str (not "int") to str

new_char = len(input("what is your name: "))
#converted int into str
new_num_char = str(new_char)
print("your name has "+new_num_char+" characters")

a = str(123)
print(type(a))
print(40+float("70"))
#float add 40+70
print(str(5)+str(5))

