from itertools import count

print("** day 5 of coding")
print("for looping")
fruits = ["apple","peach","pear"]
for fruit in fruits:
    print(fruit)
    # print(fruit + " apple")
print()
print("* student score *")
student_score = [124,424,24,845,454,545,5,45,454,5,4,5,45,4,3,33,5545,5,545,45]
total_score = sum(student_score)
# 1 option
# print(total_score)

sum = 0
for score in student_score:
    sum += score
print(sum)
print()
print("**  max() **")
max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
        # print(max_score)
print(max_score)
print()

print("** add numbers in loop with range() function")
number = 0
for i in range(100):
    number += i+1
print(number)





