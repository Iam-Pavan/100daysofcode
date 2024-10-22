import random

small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@']

print("welcome to the PyPassword generator!")
nr_letters = int(input("how many letters would you like in your password\n"))
nr_numbers = int(input("how many numbers would you like \n"))
# easy Level
password = ""
nr_symbols = int(input("how many symbols would you like \n"))


# nr_letters = 4
# for char in range(1, nr_letters+1):
#     password += random.choice(small_letters)
# for char in range(1, nr_numbers+1):
#     password += random.choice(numbers)
# for char in range(1, nr_symbols+1):
#     password += random.choice(symbols)
# print(password)

# hard level
password_list = []
for char in range(1, nr_letters+1):
    password_list.append(random.choice(small_letters))
for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))
for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
# print(password_list)
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"your password is {password}")
