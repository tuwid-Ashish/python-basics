# Write a program that takes a number from the user and prints the sum of all even numbers from 1 to that number.

num = int(input("Enter a number: "))

even_number_sum = 0
for i in range( 1,num+1) :
    if i % 2 == 0:
        even_number_sum += i
print("Sum of even numbers: ", even_number_sum)  


# Write a program that takes a number from the user and prints whether the number is prime or not.

if num > 1: 
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")