import  random
from random import shuffle

# import pizza_order_practice
# print(pizza_order_practice.pizza_size)

# friend = ["makara","bakara","thepura","daddhoba"]
# choices = random.randint(0,3)
# print(friend[choices])
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&']

print("welcome to the PyPassword generator!")
nr_letters = int(input("how many letters would you like in your password: "))
nr_symbols = int(input("how many symbols would you like: "))
nr_numbers = int(input("how many numbers would you like: "))

# easy level
# password = ""
#
# for char in range(0, nr_letters):
#     random_char = random.choice(letters)
# for char in range(0, nr_symbols):
#     password += random.choice(numbers)
# for char in range(0, nr_numbers):
#     password += random.choice(symbols)
# print(password)

#hard level
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(numbers))
for char in range(0, nr_numbers):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is {password}")




