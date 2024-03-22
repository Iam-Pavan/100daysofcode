print("control flow with if/else and conditional operators\n")
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


print("interact with exercising code\n")

# which number do you want to check
print("enter and check the number is odd or even")
numbers = int(input(": "))
# if the number can be divided by 2 with 0 remainder
if numbers % 2 == 0:
    print("this is an even number.")
else:
    print("this is an odd number.")

#