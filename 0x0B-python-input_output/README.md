Python Input/Output (I/O) refers to the process of interacting with external data sources such as files, databases, network connections, and user input/output. It involves reading data from these sources into a program (input) or writing data from a program to these sources (output).

Input:
Python provides several ways to read input from the user. The most commonly used function for this purpose is input(), which allows the program to wait for the user to enter a line of text. The input() function returns the user's input as a string, which can be stored in a variable for further processing.

Output:
Python provides various mechanisms for displaying output to the user. The most common way is by using the print() function, which allows you to print text, variables, and expressions to the console. The print() function automatically appends a newline character at the end of each line by default.

File Input/Output:
Python offers built-in functions and modules for working with files. You can open a file using the open() function, specifying the file's name and the mode in which you want to open it (e.g., read, write, append). Once a file is opened, you can read its contents using methods like read(), readline(), or readlines(), and write data to it using the write() or writelines() methods.

Standard I/O Streams:
Python provides three standard I/O streams: stdin, stdout, and stderr. stdin is used for input, stdout is used for normal output, and stderr is used for error messages. These streams are automatically available to your program without the need for explicit file handling.

Serialization:
Python supports object serialization, which allows you to convert complex objects into a format suitable for storage or transmission. The pickle module provides functions for serializing and deserializing Python objects into a binary format. JSON (JavaScript Object Notation) is another popular serialization format supported by the json module.

Database Input/Output:
Python provides various libraries and modules to interact with databases, such as SQLite, MySQL, and PostgreSQL. These libraries allow you to establish connections, execute queries, and retrieve data from databases.

Network Input/Output:
Python's socket module enables network communication, allowing you to create network connections, send and receive data over protocols such as TCP and UDP. The requests library is commonly used for making HTTP requests and interacting with web services.

In summary, Python's Input/Output capabilities encompass reading user input, displaying output, working with files, handling standard I/O streams, serialization, database interactions, and network communication. These functionalities empower Python developers to build versatile and interactive programs

0. Read file
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that reads a text file (UTF8) and prints it to stdout:

Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.

1. Write to a file
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

Prototype: def write_file(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.

2. Append to a file
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

Prototype: def append_write(filename="", text=""):
If the file doesn’t exist, it should be created
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.

3. To JSON string
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that returns the JSON representation of an object (string):

Prototype: def to_json_string(my_obj):
You don’t need to manage exceptions if the object can’t be serialized.

4. From JSON string to Object
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that returns an object (Python data structure) represented by a JSON string:

Prototype: def from_json_string(my_str):
You don’t need to manage exceptions if the JSON string doesn’t represent an object.

5. Save Object to a file
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that writes an Object to a text file, using a JSON representation:

Prototype: def save_to_json_file(my_obj, filename):
You must use the with statement
You don’t need to manage exceptions if the object can’t be serialized.
You don’t need to manage file permission exceptions.

6. Create object from a JSON file
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that creates an Object from a “JSON file”:

Prototype: def load_from_json_file(filename):
You must use the with statement
You don’t need to manage exceptions if the JSON string doesn’t represent an object.
You don’t need to manage file permissions / exceptions.

7. Load, add, save
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that adds all arguments to a Python list, and then save them to a file:

You must use your function save_to_json_file from 5-save_to_json_file.py
You must use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions.

8. Class to JSON
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

Prototype: def class_to_json(obj):
obj is an instance of a Class
All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
You are not allowed to import any module

9. Student to JSON
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Student that defines a student by:

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
You are not allowed to import any module

10. Student to JSON with filter
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Student that defines a student by: (based on 9-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module

11. Student to disk and reload
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Student that defines a student by: (based on 10-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attributes name contain in this list must be retrieved.
Otherwise, all attributes must be retrieved
Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
You can assume json will always be a dictionary
A dictionary key will be the public attribute name
A dictionary value will be the value of the public attribute
You are not allowed to import any module
Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

12. Pascal's Triangle
mandatory
Score: 0.0% (Checks completed: 0.0%)
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module

13. Search and update
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

Prototype: def append_after(filename="", search_string="", new_string=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module13. Search and update
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

Prototype: def append_after(filename="", search_string="", new_string=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module


14. Log parsing
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

































.

