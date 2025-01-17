# Write a program to find the factorial of a given number.

num = int(input("Enter a number: "))
factorical_num = 1
while num > 0:
    factorical_num = factorical_num * num
    num -= 1
print("Factorial of the given number is: ", factorical_num)