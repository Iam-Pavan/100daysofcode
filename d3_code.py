print("control flow with if/elif/else and conditional operators\n")
print("comparison operators ==\n > or <\n >= or <=\n != \n  ")
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?: "))

if height == 120:
    print("----your can ride the rollercoaster")
    age = int(input("your age: "))
    if age < 12:
        print("you pay $5.")
    elif age <= 18:
        print("you pay $7")
    else:
        print("you pay $12")
else:
    print("sorry, you have to grow taller before you can ride.")


print("****interact with exercising code\n")

# which number do you want to check
print("enter and check the number is odd or even")
numbers = int(input(": "))
# if the number can be divided by 2 with 0 remainder
if numbers % 2 == 0:
    print("this is an even number.")
else:
    print("this is an odd number\n.")
print("interact with exercising code\n")

print("check leap year")
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")
print("----multiple if statements in succession")
print("-----ogical operators= and or not")
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?: "))
bill = 0
if height >= 120:
    print("----your can ride the rollercoaster")
    age = int(input("your age: "))
    if age < 12:
        bill = 5
        print("child ticket pay $5.")
    elif age <= 18:
        bill = 7
        print("youth ticket pay $7")
    elif age >= 45 and age <= 55:
        print("everything is ok going to be ok . have a free ride on us")
    else:
        bill = 12
        print("adult ticket pay $12")

    wants_photo = input("do you want a photo taken? y or n.: ")
    if wants_photo == "y":
        bill += 3
    print(f"your final bill is ${bill}")
else:
    print("sorry, you have to grow taller before you can ride.\n")

print("****interact with exercising code\n")
print("pizza order practice\n")
print("thank you for choosing python pizza deliveries ")
size = input("size \"s\": ")
add_pepperoni = input("add_pepperoni y or n: ")
extra_cheese = input("extra_cheese y or n: ")

bill = 0

if size == "s":
    bill +=15
elif size == "m":
    bill +=20
else:
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill +=2
    else:
        bill +=3
if extra_cheese == "y":
   bill += 1
print(f"your final bill is ${bill}.\n")
print("*****interact with exercising code\n")
print("the love calculator is calculating your score.... ")
name1 = input("wht is ur name: ")
name2 = input("wht is their name: ")

combined_names = name1 + name2
lower_names  = combined_names.lower()
t=lower_names.count("t")
r=lower_names.count("r")
u=lower_names.count("u")
e=lower_names.count("e")
first_digit = t+r+u+e
print(first_digit)
l=lower_names.count("l")
o=lower_names.count("o")
v=lower_names.count("v")
e=lower_names.count("e")
second_digit = l+o+v+e
print(second_digit)
score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"your score is {score}, you go together like coke mentos ")
elif(score >= 40) and (score <= 50):
    print(f"your score is {score}, you are alright together")
else:
 print(f"your score is {score}.")

