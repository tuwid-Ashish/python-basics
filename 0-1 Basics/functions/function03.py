def multiply(n,m):
    if isinstance(n, str) and isinstance(m, str):
        return "Please enter a number", n+ m
    return n * m

print(multiply(5,5))
print(multiply("the number is : ","5"))