# write a program that asks the user for their age and then prints out a message based on the age.
user_age = input("Enter your age: ")
age = int(user_age)

if(age<13):
    print("You are a child")
    
elif age<20:
    print("You are a teenager")
elif age <60:
    print("You are an adult")
else:
    print("you are a senior citizen")   