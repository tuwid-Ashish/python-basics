# Python Basics Morning Class Notes

## Introduction to Python Basics
Welcome to the Python Basics class! Today, we will learn foundational programming concepts such as loops, conditionals, functions, and basic data structures like tuples and sets. This class is designed for beginners, so we will use simple data types like numbers and strings for problem-solving.

---

## Loops
Loops allow us to repeat a block of code multiple times. Let's explore some examples:

1. Print numbers from 1 to 10 using a loop.
   ```python
   for i in range(1, 11):
       print(i)
   ```

2. Calculate the sum of all even numbers between 1 and 20.
   ```python
   total = 0
   for i in range(1, 21):
       if i % 2 == 0:
           total += i
   print(total)
   ```

3. Print each character of the string "Python" on a new line.
   ```python
   for char in "Python":
       print(char)
   ```

4. Count the number of vowels in the string: `"programming is fun"`.
   ```python
   string = "programming is fun"
   vowels = "aeiou"
   count = 0
   for char in string:
       if char in vowels:
           count += 1
   print(count)
   ```

5. Find the factorial of a number using a loop.
   ```python
   num = 5  # Example number
   factorial = 1
   for i in range(1, num + 1):
       factorial *= i
   print(factorial)
   ```

6. Create a program that repeatedly asks for user input until the user types "stop".
   ```python
   while True:
       user_input = input("Enter something (type 'stop' to quit): ")
       if user_input.lower() == "stop":
           break
   ```

---

## Conditionals
Conditionals allow us to make decisions in our code. Here are some examples:

1. Check if a number is positive, negative, or zero.
   ```python
   num = int(input("Enter a number: "))
   if num > 0:
       print("Positive")
   elif num < 0:
       print("Negative")
   else:
       print("Zero")
   ```

2. Determine if a number is even or odd.
   ```python
   num = int(input("Enter a number: "))
   if num % 2 == 0:
       print("Even")
   else:
       print("Odd")
   ```

3. Check if a string starts with the letter 'P'.
   ```python
   string = input("Enter a string: ")
   if string.startswith("P"):
       print("Yes, it starts with 'P'")
   else:
       print("No, it does not start with 'P'")
   ```

4. Verify if the string "hello world" contains the word "hello".
   ```python
   string = "hello world"
   if "hello" in string:
       print("Yes, 'hello' is in the string")
   else:
       print("No, 'hello' is not in the string")
   ```

5. Compare two numbers and print the larger one.
   ```python
   num1 = int(input("Enter the first number: "))
   num2 = int(input("Enter the second number: "))
   if num1 > num2:
       print(f"The larger number is {num1}")
   elif num2 > num1:
       print(f"The larger number is {num2}")
   else:
       print("Both numbers are equal")
   ```

6. Check if a number is divisible by both 3 and 5.
   ```python
   num = int(input("Enter a number: "))
   if num % 3 == 0 and num % 5 == 0:
       print("Yes, divisible by both 3 and 5")
   else:
       print("No, not divisible by both 3 and 5")
   ```

---

## Functions
Functions help us organize code into reusable blocks. Practice the following:

1. Create a function that takes a number and returns its square.
   ```python
   def square(num):
       return num ** 2
   print(square(4))
   ```

2. Write a function to greet a user by their name.
   ```python
   def greet(name):
       print(f"Hello, {name}!")
   greet("Alice")
   ```

3. Create a function to find the length of a string.
   ```python
   def string_length(string):
       return len(string)
   print(string_length("Python"))
   ```

4. Write a function that takes two numbers and returns their sum.
   ```python
   def add_numbers(a, b):
       return a + b
   print(add_numbers(3, 5))
   ```

5. Check if a string is a palindrome.
   ```python
   def is_palindrome(string):
       return string == string[::-1]
   print(is_palindrome("madam"))
   ```

6. Find the maximum of three numbers using a function.
   ```python
   def max_of_three(a, b, c):
       return max(a, b, c)
   print(max_of_three(10, 20, 15))
   ```

---

## Tuples and Sets
Tuples and sets are simple but essential data structures in Python. Let’s explore them:

### Tuples
1. Access the second and last elements of the tuple `(10, 20, 30, 40)`.
   ```python
   my_tuple = (10, 20, 30, 40)
   print(my_tuple[1])  # Second element
   print(my_tuple[-1])  # Last element
   ```

### Sets
2. Find the union and intersection of two sets: `{1, 2, 3}` and `{3, 4, 5}`.
   ```python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   print(set1.union(set2))  # Union
   print(set1.intersection(set2))  # Intersection
   ```

---

## Additional Topics (Optional)
If time permits, we will briefly cover:

1. **Variables and Data Types**: Learn how to store and manipulate numbers and strings.
2. **Input and Output**: Write programs that take user input and display results.
3. **String Manipulation**: Explore string slicing and methods like `.upper()`, `.lower()`, and `.replace()`.
4. **Basic Math Operations**: Solve problems using addition, subtraction, multiplication, and division.

---

## Closing
Feel free to ask questions during the class. Let’s make programming fun and interactive! 🚀

