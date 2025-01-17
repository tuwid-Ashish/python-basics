# write a program that reads two numbers from the user and prints the larger number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"The larger number is {num1}")
elif num2 > num1:
    print(f"The larger number is {num2}")
else:
    print("Both numbers are equal")