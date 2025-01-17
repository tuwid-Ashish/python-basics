# Write a program that takes a string from the user and prints the reverse of the string.

user_str = input("Enter a string: ")
reverserd_str = ""
for i in user_str:
    reverserd_str = i + reverserd_str

print(reverserd_str)