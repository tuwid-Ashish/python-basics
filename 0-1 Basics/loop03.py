num = int(input("Enter a number: "))

for i in range(1,10):
    if i == 5:
        continue
    multiplication = num * i
    print(num, "x", i, "=", multiplication)