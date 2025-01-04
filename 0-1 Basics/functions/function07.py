def print_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_args(name="John", age=25, city="New York")
    