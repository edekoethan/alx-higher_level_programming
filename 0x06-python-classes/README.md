Python is an object-oriented programming language, which means it allows you to define and use classes and objects. Classes are blueprints or templates that define the structure and behavior of objects, while objects are instances of those classes.

In Python, you define a class using the class keyword, followed by the class name. Within a class, you can define attributes (variables) and methods (functions). Attributes store data associated with objects, while methods define the actions or behaviors that objects can perform.

To create an object from a class, you use the class name followed by parentheses. This calls the class's constructor, which initializes the object and sets its initial state. You can then access the attributes and call the methods of the object using dot notation.

Python also provides a special method called __init__(), which is called automatically when an object is created. This method allows you to set the initial values of the object's attributes. Additionally, there are other special methods, such as __str__() and __repr__(), which provide string representations of objects.

You can create multiple objects from the same class, and each object maintains its own separate state. This allows you to work with different instances of a class, each with its own set of attributes and behaviors.

Inheritance is another important concept in object-oriented programming. It allows you to create new classes (child classes) based on existing classes (parent classes). The child class inherits the attributes and methods of the parent class, allowing you to reuse code and extend functionality.

Polymorphism is another feature of object-oriented programming, which means that objects of different classes can be used interchangeably if they have a common interface or superclass. This allows you to write more flexible and modular code.

Overall, classes and objects in Python provide a powerful way to organize and structure your code, allowing you to create reusable and modular components.




Tasks
0. My first square
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write an empty class Square that defines a square


1. Square with size
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
:

2. Size validation
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 1-square.py)

3. Area of a square
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 2-square.py)

4. Access and update private attribute
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 3-square.py)

5. Printing a square
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 4-square.py)

6. Coordinates of a square
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 5-square.py)

7. Singly linked list
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a class Node that defines a node of a singly linked list by:

Private instance attribute: data:
property def data(self): to retrieve it
property setter def data(self, value): to set it:
data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
Private instance attribute: next_node:
property def next_node(self): to retrieve it
property setter def next_node(self, value): to set it:
next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
Instantiation with data and next_node: def __init__(self, data, next_node=None):

8. Print Square instance
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 6-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integer
Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space
Printing a Square instance should have the same behavior as my_print()



9. Compare 2 squares
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be a number (float or integer), otherwise raise a TypeError exception with the message size must be a number
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area

10. ByteCode -> Python #5
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write the Python class MagicClass that does exactly the same as the following Python bytecode:
