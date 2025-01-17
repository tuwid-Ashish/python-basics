# Write a Python program to find the first duplicate character in a given string.
user_str = input("Enter a string: ")

for i in user_str:
    if user_str.count(i)> 1:
        print(i, "is a duplicate character")
        break