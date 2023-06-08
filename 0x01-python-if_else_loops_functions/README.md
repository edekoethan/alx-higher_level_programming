Python provides several essential programming constructs that are commonly used for control flow and modular code organization. Let's briefly discuss if/else statements, loops, and functions in Python.

If/else statements:

If/else statements are used for conditional execution of code based on a certain condition.

The if statement checks a condition and executes a block of code if the condition is true.

The else statement is optional and provides an alternative block of code to be executed if the condition in the if statement is false.

The elif (short for "else if") statement can be used to add additional conditions to check.

Here's an example:

python
Copy code
x = 10
if x > 0:
    print("Positive number")
elif x < 0:
    print("Negative number")
else:
    print("Zero")
Loops:

Loops allow you to repeatedly execute a block of code until a certain condition is met.

Python offers two main types of loops: for and while.

The for loop is used when you have a known number of iterations or when iterating over an iterable object.

The while loop is used when you want to repeat a block of code until a specific condition is no longer true.

Here are examples of both types of loops:

python
Copy code
# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
x = 0
while x < 5:
    print(x)
    x += 1
Functions:

Functions are blocks of reusable code that perform a specific task.

They allow you to organize your code, make it more modular, and avoid code repetition.

Functions can have parameters (inputs) and return a value (output), although both are optional.

Here's an example of a function that calculates the factorial of a number:

python
Copy code
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120
In the example above, the factorial() function takes a number n as input and returns the factorial of n.

These are foundational concepts in Python programming that are used extensively in various applications. Understanding if/else statements, loops, and functions allows you to write more flexible and organized code to solve a wide range of problems


0. Positive anything is better than negative nothing
mandatory
Score: 0.0% (Checks completed: 0.0%)
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.




1. The last digit
mandatory
Score: 0.0% (Checks completed: 0.0%)
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.


2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.



3. When I was having that alphabet soup, I never thought that it would pay off
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.


4. Hexadecimal printing
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)


5. 00...99
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a program that prints numbers from 0 to 99.


6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a program that prints all possible different combinations of two digits.


7. islower
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that checks for lowercase character.


8. To uppercase
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that prints a string in uppercase followed by a new line.

9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that prints the last digit of a number.

10. a + b
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that adds two integers and returns the result.


11. a ^ b
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that computes a to the power of b and return the value.




12. Fizz Buzz
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that prints the numbers from 1 to 100 separated by a space.

For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz.



.
