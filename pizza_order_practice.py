print("welcome to python pizza order")
print("** order now! **")
pizza_size = input("enter size of the pizza like 's','m' or 'l': ")
bill = 0
if pizza_size == 's':
    bill += 100
elif pizza_size == "m":
    bill += 150
elif pizza_size == "l":
    bill += 200
else:
    print("you typed invalid size")
print(f"your payable bill is ${bill}")

add_items = input("add items choose 'y' for yes and 'n' for no:  ")
if add_items == 'y':
    add_cheese = input("cheese 's' for $20 'm' for $30 'l' for $40 you add quantity line(+1): " )
    if add_cheese and pizza_size == "s":
        bill += 20
    elif add_cheese and pizza_size == "m":
        bill += 30
    elif add_cheese and pizza_size == "l":
        bill += 40
    else:
        print(f"your payable bill is ${bill}")
    add_juice_item = input("add juice items choose 'y' for yes and 'n' for no:  ")
    if add_juice_item == "y":
        add_juice = int(input("juice for $30 only coca-cola you add quantity line(+1): "))
        if add_juice > 0:
            bill += 30
        else:
            print("ok thanks!")
    print(f"your payable bill is ${bill}")
else:
    print("ok thanks for coming!")