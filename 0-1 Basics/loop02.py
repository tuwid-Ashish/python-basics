num = int(input("Enter a number: "))

even_number_sunm = 0
for i in range( 1,num+1) :
    if i % 2 == 0:
        even_number_sunm += i
print("Sum of even numbers: ", even_number_sunm)  
# if num > 1: 
#     for i in range(2,num):
#         if (num % i) == 0:
#             print(num,"is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")