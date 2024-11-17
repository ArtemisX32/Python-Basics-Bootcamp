# Python-Basics-Bootcamp

Lesson 1: Setting Up Your Environment
_______________________________________
Download Python: Go to the official Python website and download the latest version.

Install VS Code: Install Visual Studio Code from here.

Install Python Extension for VS Code: In VS Code, search for "Python" in the Extensions panel and install the official Python extension by Microsoft.

Create a Python Workspace:

Create a folder named python_course.
Inside the folder, create a file named hello_world.py for your first Python script.
Open the folder in VS Code.
Run Your First Python Code:

In the hello_world.py file, write:
python
Copy code
print("Hello, World!")
Press Ctrl + Alt + N (or click on "Run Code" if you have the Code Runner extension installed) to run the script.
___________________________________________________________________________________________________________________________________________________________

Variables and Data types
________________________
Python uses dynamic typing, so you dont need to declare variable types explicitly. Let's cover the basics:

1. String: text enclosed in quotes.
        name = "Alice"

2. Integer: Whole numbers.
        age = 25

3. Float: Decimal Numbers.
        height: 5.9

4. Boolean: True or False values.
        is_student = True

5. List: Ordered collection of items(can be mixed types).
        hobbies =["reading", "traveling", "coding"]

6. Tuple: Immutable ordered collection.
        coordinates = (10, 20)

______________________________________________________________________________________________________________

Operations

________________________

1. Arithmetic Operations:

        a = 10
        b = 5
        sum = a + b # Addition
        difference = a - b  # Subtraction
        product = a * b  # Multiplication
        quotient = a / b  # Division
        modulus = a % b  # Modulus
        power = a ** b  # Exponentiation

Example: calculator.py a basic interpation of a calculator.

        # Simple Calculator
        a = 10
        b = 5
        print(f"Sum: {a + b}")
        print(f"Difference: {a - b}")
        print(f"Product: {a * b}")
        print(f"Quotient: {a / b}")
        print(f"Modulus: {a % b}")
___________________________________________________________________________________________________________________________________________________________

Lesson 3: Control Flow (if, elif, else)
_______________________________________
In Python, control flow is managed through if, elif, and else statements.

Syntax:

        if condition:
            # Execute this block
        elif another_condition:
            # Execute this block
        else:
            # Execute this block if no previous condition was true

Example: Create a file if_elif_else.py:

        age = 18
        if age >= 18:
        print("You are an adult.")
        elif age == 17:
        print("You are almost an adult.")
        else:
        print("You are a minor.")
___________________________________________________________________________________________________________________________________________________________

Lesson 4: Loops (for, while)
_____________________________
for Loop: Used for iterating over a sequence (list, tuple, etc.)

        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
                print(fruit)

while Loop: Repeats as long as a condition is true.

        counter = 0
        while counter < 5:
                print(counter)
                counter += 1 #Increment 

Example: Create a file loop.py:

        # for loop
        for i in range(1, 6):
    print(i)

        # while loop
        count = 0
        while count < 3:
                print("Count is:", count)
                count += 1  
___________________________________________________________________________________________________________________________________________________________


Lesson 5: Functions
________________________
Functions allow you to reuse code and make it more modular.

Function Syntax:

        def function_name(parameters):
                #Function Body
                return value

Example: Create a file function.py:

        def greet(name):
                return f"Hello, {name}!"

        print(greet("Alice"))

___________________________________________________________________________________________________________________________________________________________

Lesson 6: Data Structures (Lists, Dictionaries, Sets, Tuples)
______________________________________________________________
Lists:

Ordered and changeable collection.

        fruits = ["apple", "banana", "cherry"]
        fruits.append("orange")  # Adds 'orange' to the list

Dictionaries:
Key-value pairs (hash map).

        student = {"name": "John", "age": 25, "course": "Python"}
        print(student["name"])  # John

Sets:
Unordered collection of unique items.

        fruits = {"apple", "banana", "cherry"}
        fruits.add("orange")  # Adds 'orange'

Tuples:
Immutable ordered collection.

        coordinates = (10, 20)

___________________________________________________________________________________________________________________________________________________________

Lesson 7: File Handling
________________________
Python allows you to read from and write to files.

Opening a File

        file = open("example.txt", "w")  # 'w' is write mode
        file.write("Hello, world!")
        file.close()  # Don't forget to close the file

Reading from a File:

        file = open("example.txt", "r")  # 'r' is read mode
        content = file.read()
        print(content)
        file.close()

___________________________________________________________________________________________________________________________________________________________

Lesson 8: Error Handling (try, except)
________________________________________
Python uses {try} and {except} blocks to handle errors.

Syntax:

        try:
                # Code that might raise an error
        except ExceptionType as e:
                # Code to handle the error
                print(f"Error occurred: {e}")

Example: create file try_except.py:

        try:
                x = 10 / 0
        except ZeroDivisionError as e:
                print("Cannot divide by zero!")

___________________________________________________________________________________________________________________________________________________________

Lesson 9: Classes and Objects (OOP)
_____________________________________
Python supports object-oriented programming (OOP).

Class Syntax:

        class Person:
                def __init__(self, name, age):
                        self.name = name
                        self.age = age

        def greet(self):
                print(f"Hello, my name is {self.name} and I am {self.age} years old.")

        # Create an object
        person1 = Person("Alice", 25)
        person1.greet()  # Output: Hello, my name is Alice and I am 25 years old.

___________________________________________________________________________________________________________________________________________________________

Lesson 10: Advanced Topics (List Comprehensions, Lambda Functions)
____________________________________________________________________
List Comprehensions:
A concise way to create lists.

        squares = [x**2 for x in range(5)]
        print(squares)

Lambda Functions:
Small anonymous functions.

        square = lambda x: x**2
        print(square(5))  # Output: 25

___________________________________________________________________________________________________________________________________________________________

Final Project: Build a To-Do List Application
        1. Create a file todo.py.
        2. Define functions for adding, listing, and removing tasks.
        3.Store tasks in a list and print them to the console.
        4. Handle basic exceptions like empty lists.

___________________________________________________________________________________________________________________________________________________________

Extra Resources:

        https://docs.python.org/3/
        https://realpython.com/
        https://automatetheboringstuff.com/
