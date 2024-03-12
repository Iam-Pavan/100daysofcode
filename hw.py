#hello world program
#output function print()
print("hello world")
var = 19

print(type(var),var)

Email = str(input("enter email: "))
print("password must and should in numbers")

password = int(input("create your password: "))
print("your email ",Email,"and your password ",password)

print("enter again for check your mail and password")

rEmail = str(input("enter email: "))
print("enter previous password must and should in same")

rpassword = int(input("create your password: "))
print("your email ",rEmail,"and your password",rpassword)

if(Email == rEmail and password == rpassword):
    print("good job!, you are verified")
    print("your Email is: ",rEmail)
    print("your password is: ",password)



