# Write a program that takes a number from the user and prints the multiplication table of that number, except for the number 5.
num = int(input("Enter a number: "))

for i in range(1,10):
    if i == 5:
        continue
    multiplication = num * i
    print(num, "x", i, "=", multiplication)