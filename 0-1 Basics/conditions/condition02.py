# Write a program that asks the user for their age and the day of the week they want to go to the movies.
user_age = input("Enter your age : ")
age = int(user_age)

day = input("Enter the day of the week: ")

price = 12 if age>=18 else 8

if day == "wednesday":
    price = price - 2

print("ticket price for you $", price)

# if age< 18:
#     if day == "wednesday":
#         print("you have to pay $6 for movie ticket")
#     else:
#         print("you have to pay $8 for movie ticket")
# else :
#     if day == "wednesday":
#         print("you have to pay $11 for movie ticket")
#     else:  
#         print("you have to pay $13 for movie ticket")

 