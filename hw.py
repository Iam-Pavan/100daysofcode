#hello world program
#output function print()
print("hello world")

print("**  login form  **")
Email = str(input("enter email: "))
print("password must and should in numbers")

password = int(input("create your password: "))
print("your email ",Email,"and your password ",password)

print("enter again for check your mail and password is right")
print("--------------------------------")

rEmail = str(input("enter email: "))
print("enter previous password must and should in same")

rpassword = int(input("create your password: "))
print("your email ",rEmail,"and your password",rpassword)

if(Email == rEmail and password == rpassword):
    print("good job!, you are verified")
    print("your Email is: ",rEmail)
    print("your password is: ",password)
else:
    print("****you entered wrong password plz check it again")



