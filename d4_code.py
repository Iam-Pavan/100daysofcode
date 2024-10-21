import random
import random as r

from userpath.cli import append

# random interger
print("**** random numbers")
random_integer = r.randint(1,10)
print(random_integer)

print()
print("**** random numbers float ")
random_float_number = random.random() * 10
print(random_float_number)

print()
print("**** random uniform numbers")
random_uniform = random.uniform(1,10)
print(random_uniform)

print()
print("**** random heads and tails")
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("head")
else:
    print("tails")
# print(random_heads_or_tails)
print()
print("lists")
fruits = ["apple","banana","orange","grapes"]
print(fruits[2])
print(fruits)
print()

print("**replace the value")
fruits[1] = "onion"
print(fruits)
print()

print("** append the value")
fruits.append("tomato")
print(fruits)
print()

print("** append the value")
fruits.extend(["ramesh","govind"])
print(fruits)

