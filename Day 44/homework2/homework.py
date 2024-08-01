# This script prints "Hello, World!" to the console
print("Hello, World!")


# This script takes user input and prints it
user_input = input("Enter something: ")
print("You entered:", user_input)

# This is a single-line comment
"""
This is a multi-line comment.
It spans multiple lines.
"""
print("Comments demonstration")

# This script demonstrates indentation in Python
for i in range(5):
    print("Number:", i)

# This script shows how to break lines in Python
total = 1 + 2 + 3 + \
        4 + 5 + 6
print("Total:", total)

# This script prints "Hello, World!" to the console
print("Hello, World!")  # Print statement



# This script defines a function to add two numbers
def add_numbers(a, b):
    # The function adds two numbers and returns the result
    return a + b

# Call the function and print the result
result = add_numbers(5, 3)
print("Result:", result)

"""
This script demonstrates the use of comments in Python.
It includes examples of single-line comments, multi-line comments,
and block comments.
"""
print("Comments demonstration")

# This script demonstrates disabling part of the script using comments
print("This will be printed")
# print("This will not be printed")



# This script contains intentional errors
print("This will be printed")
# The following line has a syntax error because of the missing quote
# print("This will cause an error)

# Initializing variables of different data types
integer_var = 10
float_var = 10.5
string_var = "Hello"
boolean_var = True

# Swapping values of two variables
a = 5
b = 10
a, b = b, a
print("a:", a, "b:", b)

# Taking user input to assign values to variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Name:", name, "Age:", age)

# This script demonstrates the use of global and local variables
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(local_var)
    print(global_var)

my_function()
print(global_var)
# print(local_var)  # This will cause an error because local_var is not defined outside the function



# Variable naming conventions
snake_case_variable = "snake_case"
camelCaseVariable = "camelCase"
PascalCaseVariable = "PascalCase"


# Variables of different data types
integer = 10
float = 10.5
string = "Hello"
boolean = True



# Converting between different data types
integer_var = 10
float_var = float(integer_var)
string_var = str(integer_var)
boolean_var = bool(integer_var)


# Using type() function to check variable types
print(type(10))       # int
print(type(10.5))     # float
print(type("Hello"))  # str
print(type(True))     # bool



# Basic arithmetic operations
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)



# Comparing different data types using relational operators
print(10 > 5)           # True
print(10 == 10.0)       # True (int and float comparison)
print("Hello" == "Hi")  # False



# Arithmetic operations
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)



# Generating a random number between 1 and 100
random_number = (1, 100)
print("Random Number:", random_number)




# Calculating the square root of a number
number = 16
sqrt = t(number)
print("Square Root:", sqrt)




# Finding the GCD of two numbers
a = 60
b = 48
gcd = (a, b)
print("GCD:", gcd)



# Converting integers to floats and vice versa
int_var = 10
float_var = float(int_var)
int_var_again = int(float_var)



# Converting strings to integers and floats
str_var = "10"
int_var = int(str_var)
float_var = float(str_var)



# Casting between lists and tuples
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
my_list_again = list(my_tuple)



# Handling casting errors
str_var = "Hello"
try:
    int_var = int(str_var)
except ValueError:
    print("Cannot convert string to int")



# Converting a string representing a number to an integer
str_var = "123"
int_var = int(str_var)
print("Integer value:", int_var)



# This script demonstrates the use of boolean values
a = True
b = False
print("a:", a)
print("b:", b)



# This script performs logical operations
a = True
b = False
print("a and b:", a and b)  # False
print("a or b:", a or b)    # True
print("not a:", not a)      # False

# This script uses comparison operators to return boolean values
x = 10
y = 20
print("x == y:", x == y)    # False
print("x != y:", x != y)    # True
print("x > y:", x > y)      # False
print("x < y:", x < y)      # True
print("x >= y:", x >= y)    # False
print("x <= y:", x <= y)    # True

# This script uses if-else statements based on boolean values
a = True
if a:
    print("a is True")
else:
    print("a is False")

# This script returns a boolean result from a function
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False


# This script demonstrates arithmetic operators
a = 10
b = 5
print("Addition:", a + b)        # 15
print("Subtraction:", a - b)     # 5
print("Multiplication:", a * b)  # 50
print("Division:", a / b)        # 2.0
print("Modulus:", a % b)         # 0
print("Exponentiation:", a ** b) # 100000
print("Floor Division:", a // b) # 2

# This script uses assignment operators
a = 10
a += 5
print("a += 5:", a)  # 15
a -= 3
print("a -= 3:", a)  # 12
a *= 2
print("a *= 2:", a)  # 24
a /= 4
print("a /= 4:", a)  # 6.0
a %= 4
print("a %= 4:", a)  # 2.0
a **= 3
print("a **= 3:", a) # 8.0
a //= 2
print("a //= 2:", a) # 4.0

# This script shows the use of comparison operators
x = 10
y = 20
print("x == y:", x == y)    # False
print("x != y:", x != y)    # True
print("x > y:", x > y)      # False
print("x < y:", x < y)      # True
print("x >= y:", x >= y)    # False
print("x <= y:", x <= y)    # True

# This script demonstrates the use of logical operators
a = True
b = False
print("a and b:", a and b)  # False
print("a or b:", a or b)    # True
print("not a:", not a)      # False

# This script uses identity operators
a = [1, 2, 3]
b = a
c = a[:]
print("a is b:", a is b)        # True
print("a is c:", a is not c)    # True
print("a == c:", a == c)        # True

# This script creates and prints a list
my_list = [1, 2, 3, 4, 5]
print(my_list)

# This script adds and removes elements from a list
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print("After append:", my_list)
my_list.remove(3)
print("After remove:", my_list)

# This script sorts a list
my_list = [5, 3, 1, 4, 2]
my_list.sort()
print("Sorted list:", my_list)

# This script demonstrates the use of list comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# This script finds the length of a list
my_list = [1, 2, 3, 4, 5]
print("Length of list:", len(my_list))

# This script uses an if statement to check a condition
a = 10
if a > 5:
    print("a is greater than 5")

# This script uses an if-else statement
a = 10
if a > 15:
    print("a is greater than 15")
else:
    print("a is not greater than 15")

# This script uses an if-elif-else statement
a = 10
if a > 15:
    print("a is greater than 15")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is less than 10")

# This script demonstrates nested if statements
a = 10
if a > 5:
    if a < 15:
        print("a is between 5 and 15")

# This script uses the ternary operator
a = 10
result = "Greater than 5" if a > 5 else "Not greater than 5"
print(result)

# This script demonstrates a while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# This script uses a while loop with a break statement
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# This script uses a while loop with a continue statement
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# This script demonstrates an infinite loop and how to stop it
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break

# This script uses a while loop to iterate over a list
my_list = [1, 2, 3, 4, 5]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1




# This program uses all basic arithmetic operators
a = 10
b = 3
print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.3333...
print("Modulus:", a % b)          # 1
print("Floor Division:", a // b)  # 3
print("Exponentiation:", a ** b)  # 1000

# This script demonstrates the use of assignment operators
a = 10
a += 5
print("a += 5:", a)  # 15
a -= 3
print("a -= 3:", a)  # 12
a *= 2
print("a *= 2:", a)  # 24
a /= 4
print("a /= 4:", a)  # 6.0
a %= 4
print("a %= 4:", a)  # 2.0
a **= 3
print("a **= 3:", a) # 8.0
a //= 2
print("a //= 2:", a) # 4.0

# This program compares two numbers using comparison operators
x = 10
y = 20
print("x == y:", x == y)    # False
print("x != y:", x != y)    # True
print("x > y:", x > y)      # False
print("x < y:", x < y)      # True
print("x >= y:", x >= y)    # False
print("x <= y:", x <= y)    # True

# This script uses logical operators in a simple condition
a = True
b = False
print("a and b:", a and b)  # False
print("a or b:", a or b)    # True
print("not a:", not a)      # False


# This script shows the use of bitwise operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary
print("a & b:", a & b)  # 0000
print("a | b:", a | b)  # 1110
print("a ^ b:", a ^ b)  # 1110
print("~a:", ~a)        # -11 (two's complement)
print("a << 1:", a << 1) # 20 (10100 in binary)
print("a >> 1:", a >> 1) # 5 (0101 in binary)

# This program checks if a number is within a specified range using comparison and logical operators
num = 15
if 10 <= num <= 20:
    print("The number is within the range.")
else:
    print("The number is outside the range.")

# This script uses identity operators to compare objects and variables
a = [1, 2, 3]
b = a
c = a[:]
print("a is b:", a is b)        # True
print("a is not c:", a is not c) # True
print("a == c:", a == c)        # True

# This program uses membership operators to check if a value exists in a list
my_list = [1, 2, 3, 4, 5]
print("3 in list:", 3 in my_list)    # True
print("6 not in list:", 6 not in my_list)  # True

# This script demonstrates operator precedence by creating a complex expression
result = 10 + 5 * 2 ** 2 - (3 / 1)
print("Result:", result)  # Result: 27.0

# This program takes two user inputs and performs all the basic arithmetic operations on them
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)

# This script swaps the values of two variables without using a third variable
a = 10
b = 5
a, b = b, a
print("a:", a)  # 5
print("b:", b)  # 10



# This script creates a list of five numbers and prints the list
my_list = [1, 2, 3, 4, 5]
print(my_list)

# This script accesses elements from a list using positive and negative indexing
my_list = [10, 20, 30, 40, 50]
print("First element (positive indexing):", my_list[0])
print("Last element (negative indexing):", my_list[-1])

# This script adds, removes, and updates elements in a list
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print("After adding 6:", my_list)
my_list.remove(3)
print("After removing 3:", my_list)
my_list[2] = 10
print("After updating index 2:", my_list)

# This script concatenates two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2

# This script finds the length of a list using the len() function
my_list = [1, 2, 3, 4, 5]
print("Length of the list:", len(my_list))

# This script checks if a specified element is present in a list
my_list = [1, 2, 3, 4, 5]
element = 3
if element in my_list:
    print(f"{element} is present in the list.")
else:
    print(f"{element} is not present in the list.")

# This script slices a list and prints the sliced list
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:4]
print("Sliced list:", sliced_list)

# This script sorts a list in ascending and descending order
my_list = [3, 1, 4, 2, 5]
my_list.sort()
print("Sorted in ascending order:", my_list)
my_list.sort(reverse=True)
print("Sorted in descending order:", my_list)

# This script demonstrates the use of list comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# This script finds the maximum and minimum values in a list
my_list = [3, 1, 4, 2, 5]
print("Maximum value:", max(my_list))
print("Minimum value:", min(my_list))

# This script reverses the elements of a list
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print("Reversed list:", my_list)

# This program prints numbers from 1 to 10 using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# This script calculates the sum of the first 10 natural numbers using a while loop
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum of the first 10 natural numbers:", total)

# This program prints the multiplication table of a given number using a while loop
num = 5
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# This script finds the factorial of a number using a while loop
num = 5
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"Factorial of {num} is {factorial}")

# This program prints all even numbers between 1 and 50 using a while loop
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1

# This script reverses a given number using a while loop
num = 12345
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed number:", reversed_num)

# This program calculates the sum of digits of a number using a while loop
num = 12345
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print("Sum of digits:", total)

# This script finds the greatest common divisor (GCD) of two numbers using a while loop
a = 48
b = 18
while b:
    a, b = b, a % b
print("GCD is", a)

# This program prints the Fibonacci sequence up to a specified number using a while loop
n = 10
a, b = 0, 1
while a <= n:
    print(a)
    a, b = b, a + b

# This script prints numbers from 1 to 100, but skips numbers divisible by 5, using a while loop
i = 1
while i <= 100:
    if i % 5 == 0:
        i += 1
        continue
    print(i)
    i += 1


# This program prints each element of a list using a for loop
my_list = [1, 2, 3, 4, 5]
for element in my_list:
    print(element)

# This script prints numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

# This program calculates the sum of elements in a list using a for loop
my_list = [1, 2, 3, 4, 5]
total = 0
for element in my_list:
    total += element
print("Sum of elements:", total)

# This script prints the multiplication table of a given number using a for loop
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# This program prints all even numbers between 1 and 50 using a for loop
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# This script prints the Fibonacci sequence up to a specified number using a for loop
n = 10
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b

# This program iterates over a dictionary and prints each key-value pair
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# This script finds the maximum and minimum values in a list using a for loop
my_list = [3, 1, 4, 2, 5]
max_value = my_list[0]
min_value = my_list[0]
for num in my_list:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print("Maximum value:", max_value)
print("Minimum value:", min_value)

# This program prints each character of a string using a for loop
my_string = "Hello, World!"
for char in my_string:
    print(char)

# This script prints the reverse of a list using a for loop
my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])

# This program uses nested for loops to print a pattern, such as a triangle of stars
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# This function takes two numbers as arguments and returns their sum
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 3))  # 8

# This function checks if a given number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(11))  # True

# This function calculates the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 120

# This function returns the largest number in a list
def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

print(find_largest([3, 1, 4, 2, 5]))  # 5

# This function returns the nth Fibonacci number
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci(10))  # 55

# This function checks if a given string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # True

# This function takes a list and an element as arguments and returns the index of the element in the list
def find_index(lst, element):
    for index, value in enumerate(lst):
        if value == element:
            return index
    return -1

print(find_index([1, 2, 3, 4, 5], 3))  # 2

# This function takes a list of numbers and returns a new list with the squares of those numbers
def square_numbers(lst):
    return [x ** 2 for x in lst]

print(square_numbers([1, 2, 3, 4, 5]))  # [1, 4, 9, 16, 25]

# This function takes a string and returns the number of vowels in the string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

print(count_vowels("Hello, World!"))  # 3

# This function merges two dictionaries
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

print(merge_dicts({"a": 1, "b": 2}, {"c": 3, "d": 4}))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# This function takes a variable number of arguments and returns their sum
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # 15