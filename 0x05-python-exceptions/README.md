In Python, exceptions are a way to handle and manage errors that may occur during the execution of a program. When an exceptional situation arises, such as an error or unexpected condition, an exception is raised.

Here are key points to summarize Python exceptions:

Exception Handling: Python provides a mechanism to handle exceptions using try-except blocks. The code that might raise an exception is placed inside the try block, and the code to handle the exception is placed inside the except block.

Exception Types: Python has a variety of built-in exception types that represent different categories of errors. Some common exception types include TypeError, ValueError, NameError, and FileNotFoundError, among others. Each exception type captures specific kinds of errors and can be caught and handled separately.

Handling Multiple Exceptions: Multiple exceptions can be handled using multiple except blocks, allowing specific actions to be taken based on the type of exception raised.

Catching All Exceptions: An except block without specifying a particular exception type can be used to catch all exceptions. However, it is generally recommended to catch specific exceptions to handle them appropriately and avoid catching unintended exceptions.

Exception Propagation: If an exception is not caught within a function or block, it propagates up the call stack until it is handled by an appropriate try-except block. If an exception is never caught, it results in program termination and displays an error message.

Finally Block: A finally block can be added after the try-except blocks to define code that should be executed regardless of whether an exception occurs or not. The finally block is commonly used to release resources or perform cleanup tasks.

Raising Exceptions: Python allows raising exceptions explicitly using the raise statement. This is useful when a specific condition is met, and you want to indicate that an exceptional situation has occurred.

Custom Exceptions: Python allows defining custom exception classes by creating new classes that inherit from the base Exception class. Custom exceptions can be used to handle specific situations or create more meaningful error messages.

Overall, exceptions in Python provide a way to handle and recover from errors in a controlled manner, improving the robustness and reliability of programs by gracefully handling exceptional situations


0. Safe list printing
Write a function that prints x elements of a list.

1. Safe printing of an integers list
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that prints an integer with "{:d}".format().

2. Print and count integers
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that prints the first x elements of a list and only integers.

3. Integers division with debug
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that divides 2 integers and prints the result.

4. Divide a list
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that divides element by element 2 lists.

5. Raise exception
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that raises a type exception.

6. Raise a message
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that raises a name exception with a message.

7. Safe integer print with error message
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a function that prints an integer.

8. Safe function
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a function that executes a function safely.

9. ByteCode -> Python #4
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

10. CPython #2: PyFloatObject
#advanced
Score: 0.0% (Checks completed: 0.0%)
Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.
















.
