# Write a Python function to multiply two numbers. If the input is a string, return "Please enter a number" and the string.
def multiply(n,m):
    if isinstance(n, str) and isinstance(m, str):
        return "Please enter a number", n+ m
    return n * m

print(multiply(5,5))
print(multiply("the number is : ","5"))