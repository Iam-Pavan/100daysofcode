import random
import random as r

# random interger
print("**** random numbers")
random_integer = r.randint(1,10)
print(random_integer)

print("**** random numbers float ")
random_float_number = random.random() * 10
print(random_float_number)

print("**** random uniform numbers")
random_uniform = random.uniform(1,10)
print(random_uniform)


print("**** random heads and tails")
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("head")
else:
    print("tails")
# print(random_heads_or_tails)
