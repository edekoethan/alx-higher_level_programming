In Python, inheritance is a fundamental concept in object-oriented programming that allows classes to inherit attributes and methods from other classes. It enables the creation of hierarchical relationships between classes, where a subclass can inherit the properties and behaviors of a superclass.

Inheritance is implemented using the class keyword, where a new class is defined by specifying its superclass(es) in parentheses after the class name. The subclass inherits all the attributes and methods of its superclass(es) and can add or override them as needed.

Key points about Python inheritance:

Superclass and Subclass: The class being inherited from is called the superclass or parent class, while the class that inherits from the superclass is called the subclass or child class.

Inherited Attributes and Methods: The subclass automatically inherits all the attributes and methods of its superclass. This includes both instance variables and class variables, as well as instance methods and class methods.

Overriding Methods: If a method is defined in both the superclass and subclass with the same name, the subclass can provide its own implementation by overriding the method from the superclass. This allows customization of behavior specific to the subclass.

Adding New Attributes and Methods: The subclass can add its own attributes and methods in addition to the inherited ones, extending the functionality provided by the superclass.

Accessing Superclass Methods: The super() function is commonly used in the subclass to access and call methods from the superclass. It allows the subclass to invoke the superclass's version of the method before or after adding its own behavior.

Inheritance Hierarchies: Inheritance can be chained, allowing for the creation of multi-level inheritance hierarchies, where a subclass can itself serve as a superclass for other classes. This provides a flexible way to organize and model relationships between objects.

Inheritance promotes code reuse, modularity, and the ability to create specialized classes based on existing ones. It helps to avoid redundancy and promotes a more structured and efficient approach to designing and implementing object-oriented programs

0. Lookup
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that returns the list of available attributes and methods of an object:

Prototype: def lookup(obj):
Returns a list object

1. My list
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class MyList that inherits from list:

Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int

2. Exact same object
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):

3. Same class or inherit from
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):

4. Only sub class of
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

Prototype: def inherits_from(obj, a_class):

5. Geometry module
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write an empty class BaseGeometry.

6. Improve Geometry
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class BaseGeometry (based on 5-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented

7. Integer validator
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class BaseGeometry (based on 6-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0

8. Rectangle
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator

9. Full rectangle
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>

10. Square #1
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that inherits from Rectangle (9-rectangle.py):

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented

11. Square #2
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description: [Square] <width>/<height>

13. Can I?
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a function that adds a new attribute to an object if it’s possible:

Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
You are not allowed to use try/except
You are not allowed to import any module

























.
