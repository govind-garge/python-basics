# Basic Python Examples 🐍

**A small collection of beginner-friendly Python scripts demonstrating core language features and basic programming concepts.**

---

## Project Overview

This repository contains short, focused example scripts that show how to use Python for common tasks such as printing output, reading console input, working with lists and dictionaries, file I/O, control flow, functions, and basic object-oriented programming.

These examples are intended for learning and experimentation — you can run each script individually with Python.

---

## Prerequisites

- Python 3.8+ installed
- A terminal or command prompt

Run an example with:

```
python <script_name>.py
```

Example:

```
python basic.py
```

---

## Project Structure

- `basic.py` — Basic language features, variables, types, arithmetic, and printing.
- `console-input.py` — Reading input from the user via the console.
- `file-io.py` — Examples of reading from and writing to files.
- `demo-file-io.txt` — Sample data for file I/O examples.
- `dictionary-sets.py` — Usage of dictionaries and sets.
- `functions.py` — Defining and calling functions; examples of parameters and return values.
- `if-statement.py` — Conditional statements and branching.
- `list-tuple.py` — Lists and tuples: creation, indexing, and common operations.
- `loops.py` — `for` and `while` loop examples.
- `oops.py` — Basic object-oriented programming (classes and objects).
- `range.py` — Using `range()` for iteration.
- `string-function.py` — String operations and built-in string functions.

---

## Examples

Below are the full example snippets (copied from each script). Run any snippet by executing `python <script>.py`.

### `basic.py`

Demonstrates basic syntax: printing output, declaring variables, checking types, simple type conversions, and using arithmetic/logical/comparison operators.

```python
# Python is a case sensitive language

#print
print("hello world")

# Declare Variable
name = "Tata punch"
quantity = 5
price = 12.5
old = True
order_total = None

# print variable
print("My name is :", name)

# check variable type
print(type(name))
print(type(quantity))
print(type(price))
print(type(old))
print(type(order_total))

# Type conversion
a = int("152")
b = float("152.25")
c = str(152.25)
print("convert data types, string to integer", type(a))
print("convert data types, string to float", type(b))
print("convert data types, Float to string", type(c))

# Example
a = 10
b = 20
print("Python Arithmetic Operators a+b: ", a + b)
print("Python Logical Operators a and b: ", a and b)
print("Python Comparison Operators a == b: ", a == b)
```

---

### `console-input.py`

Shows how to read user input from the console using `input()` and use the provided value in the program.

```python
# take input from console
a = input("input from console - Enter your name:")
print("input from console - Your name is:", a)
```

---

### `file-io.py`

Covers opening files for writing/appending/reading, using `with` for context management, reading by bytes/lines, and common file modes.

```python
# Write in the file
f = open("demo-file-io.txt", "w")
f.write("Content added by code\n")
f.close()

# Append
f = open("demo-file-io.txt", "a")
f.write("Content appended by code\n")
f.close()

# a+ read and append
f = open("demo-file-io.txt", "a+")
f.write("Content appended by code\n")
data = f.read()
print("File I/O a+ read all content:", data)
f.close()

# Read all
f = open("demo-file-io.txt", "r")
data = f.read()
print("File I/O content all content:", data)
f.close()

# With context manager
with open("demo-file-io.txt", "r") as f:
    data = f.read()
    print("File I/O with and alias all content:", data)

# Read 5 characters
f = open("demo-file-io.txt", "r")
data = f.read(5)
print("File I/O content read 5 charactor:", data)
f.close()

# Single line
f = open("demo-file-io.txt", "r")
line1 = f.readline()
print("File I/O content read single line:", line1)
line2 = f.readline()
print("File I/O content read single line:", line2)
f.close()
```

---

### `dictionary-sets.py`

Shows dictionary creation and operations (nested dictionaries, access methods, updates) and basic set creation/operations.

```python
# Dictionary examples
my_dic = {}
my_dic["name"] = "Govind"

my_dictionary = {
    "name": "Govind",
    "City": "Pune",
    "mobile": 9999999999,
    "list": [1, 2, 3, 4, 5, 6, 7],
    "sub_dictionaty": {"name": "sub dictionary"}
}

print("Dictionary:", my_dictionary)
print("Get Dictionary item:", my_dictionary.get("name"))

# Set examples
my_set = {1, 2, 3, 4.5, "any string"}
print("Set in python:", my_set)
```

---

### `functions.py`

Demonstrates defining functions, default arguments, an iterative factorial implementation, recursion, and returning values.

```python
# Simple function
def sum(a, b):
    return a + b

print("Function output:", sum(10, 5))

# Default parameters
def default_sum(a=1, b=1):
    return a + b

print("Function output:", default_sum())

# Iterative factorial
def cal_factorial(n=1):
    i = 1
    factorial = 1
    while i <= n:
        factorial = factorial * i
        i += 1
    return factorial

print("Factorial Function output:", cal_factorial(5))

# Recursive example
def my_recursion(n):
    if n == 0:
        return
    print("Recursion function:", n)
    my_recursion(n - 1)

my_recursion(5)

# Factorial recursion
def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    return fact_rec(n - 1) * n

print("Factorial with Recursion function final output:", fact_rec(5))
```

---

### `if-statement.py`

Simple conditional flow example illustrating `if`, `elif`, and `else` branches and how the conditions are evaluated.

```python
age = 21
if age >= 18:
    print("if statement executed")
elif age < 18:
    print("else if statement execute")
else:
    print("invalid age")
```

---

### `list-tuple.py`

Demonstrates list creation, indexing, slicing, length and sorting, and shows tuple immutability and type.

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("type of list:", type(my_list))
my_list[7] = 1
print(my_list)
print("Slicing values from list:", my_list[0:4])
print("count of list :", len(my_list))
my_list.sort(reverse=True)
print(my_list)

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print("type of tuple:", type(my_tuple))
```

---

### `loops.py`

Examples of `while` and `for` loops, iterating lists, and control statements `break` and `continue` to influence loop flow.

```python
# While loop counter
count = 1
while count <= 5:
    print("while loop:", count)
    count += 1

# While with list
my_list = [5, 85, 5, 6, 4]
i = 0
while i < len(my_list):
    print("while loop with list:", my_list[i])
    i = i + 1

# break example
count = 1
while count <= 5:
    print("while loop with break:", count)
    if count == 3:
        break
    count += 1

# continue example
count = 1
while count <= 5:
    if count == 3:
        count += 1
        continue
    print("while loop with coutinue:", count)
    count += 1

# for loop
for el in my_list:
    print("for loop with list:", el)
else:
    print("for loop with list and else, it will execute after loop end")
```

---

### `oops.py`

Covers object-oriented concepts: classes, constructors, public/private attributes and methods, static/class methods, property, inheritance examples, and a simple `Bank_Account` demo.

```python
# Public and private attributes
class Students:
    def __init__(self, acc_no, password):
        self.acc_no = acc_no
        self.__password = password

    def __show_msg_private(self):
        msg = "this msg is from private method"
        return msg

    def show_msg_public(self):
        message = self.__show_msg_private()
        return message

student_obj = Students("223452534", "govi@#$%")
print("Student public variable:", student_obj.acc_no)
print("Student public method:", student_obj.show_msg_public())

# Operations class demo
class Operations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_val(self):
        return self.a + self.b

    def substract_val(self, val1, val2):
        return val1 - val2

    @staticmethod
    def showmsg():
        print("this is static method output")

    @staticmethod
    def multiply(x, y):
        return x * y

object1 = Operations(10, 5)
print("Add Result :", object1.add_val())
print("Substract Result :", object1.substract_val(10, 2))
object1.showmsg()
print("Static method result:", object1.multiply(5, 5))

# Inheritance examples and Bank_Account demo (see file for full details)
```

---

### `range.py`
```python
for el in range(5):
    print("for loop range with stop:", el)
for el in range(1, 10):
    print("for loop range start and stop:", el)
for el in range(2, 11, 2):
    print("for loop range start and stop and step:", el)
for el in range(10, 0, -1):
    print("for loop range Reverse:", el)
```

---

### `string-function.py`

Demonstrates string concatenation, case conversion, length, indexing and slicing, and lists common built-in string methods.

```python
# string concatenation
print("string concatination" + " hello" + " world")

a = "govind"
print("Output of String function:", a.upper())
print("Output of String Len:", len(a))
print("Access Charactor from String:", a[0])
print("Slicing Charactors from String:", a[0:4])
```

---

## Usage Tips

- Open a file in an editor and read the comments at the top — each script contains inline notes and examples.
- Modify small values and re-run to see the effects (great for learning).
- Use `python -i <script>.py` if you want to drop into an interactive session after the script runs.

---

## Contributing

Contributions are welcome! Suggested improvements:

- Add more examples for each concept (exception handling, modules, comprehensions, generators)
- Add unit tests or small exercises
- Improve documentation and add sample outputs

If you want me to add or expand a section, tell me which file or topic and I can update the repository.

---

## License

This project is provided as-is for learning purposes. Feel free to reuse and adapt the examples.

---

## 👨‍💻 Author
Created with ❤️ by Govind Garge