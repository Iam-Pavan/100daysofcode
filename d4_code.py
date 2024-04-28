import random


print("day_4")
print("random modules")
random_integer = random.randint(1, 10)
print(random_integer)

#0.0000000 - 0.99999999
random_float = random.random()
print(random_float)

print("****** random head and tail game")
#head and tail random choose
random_side = random.randint(0,1)
if random_side == 1:
    print("head")
else:
    print("Tail")

print("list")
