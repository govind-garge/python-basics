# Python

# Python is a case sensitive language

"""
# is use for single line comment and """ """ is use for multi line comment
"""

#print
print("hello world")

# Declare Veriable

name = "Tata punch"
quantity = 5
price = 12.5
old = True
order_total = None

# print veriable
print("My name is :", name)

# check veriable type, python automatically detect the data type
print(type(name))
print(type(quantity))
print(type(price))
print(type(old))
print(type(order_total))

#output
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'bool'>
#<class 'NoneType'>

#convert data types (string to integer)
a=int("152")
b=float("152.25")
c=str(152.25)
print("convert data types, string to integer", type(a))
print("convert data types, string to float", type(b))
print("convert data types, Float to string", type(c))

#Pythod reserved keywords

# False : Boolean value representing false.
# None : Represents the absence of a value or a null value.
# True : Boolean value representing true.
# and : A logical operator for Boolean AND.
# as : Used to create an alias when importing a module or in `with` statements.
# assert : Used for debugging; checks if a condition is true.
# async : Used to define an asynchronous function (coroutine).
# await : Used to pause execution and wait for an asynchronous result.
# break : Terminates the current loop (e.g., `for` or `while`).
# class : Used to define a new user-defined class.
# continue : Skips the rest of the current loop iteration and proceeds to the next.
# def : Used to define a new function.
# del : Used to delete objects or items from a list/dictionary.
# elif : Short for "else if," used in conditional statements.
# else : Used in conditional statements for the code to execute if all previous conditions are false.
# except : Used to catch exceptions in a `try...except` block.
# finally : Used in exception handling; its code always executes.
# for : Used to iterate over a sequence (e.g., a list or tuple).
# from : Used to import specific parts of a module.
# global : Declares a variable inside a function to be a global variable.
# if : Used for conditional execution.
# import : Used to import modules (external libraries).
# in : Used to check if an item is present in a sequence (membership operator) or for iteration.
# is : Used to test for object identity (identity operator).
# lambda : Used to create small, anonymous functions.
# nonlocal : Used to declare a variable inside a nested function to be in the nearest enclosing function's scope (not global).
# not : A logical operator for Boolean NOT.
# or : A logical operator for Boolean OR.
# pass : A null operation; it does nothing and is used as a placeholder.
# raise : Used to explicitly raise an exception.
# return : Used to exit a function and return a value.
# try : Used to define a block of code that may raise an exception.
# while : Used to execute a block of code repeatedly as long as a condition is true.
# with : Used to wrap the execution of a block of code with methods defined by a context manager.
# yield : Used inside a function to return a value and turn the function into a generator.

"""
Python Arithmetic Operators

Operator,Name,              "Example (a=10, b=3)",Result
+,      Addition,               a + b,              13
-,      Subtraction,            a - b,              7
*,      Multiplication,         a * b,              30
/,      Division,               a / b,              3.333...
//,     Floor Division,         a // b,             3
%,      Modulus (Remainder),    a % b,              1 
**,     Exponentiation (Power), a ** b,             103=1000

"""

# Example

a=10
b=20
print("Python Arithmetic Operators a+b: ", a+b)

"""
Python Logical Operators

Operator	Name	Example (x=True, y=False)	Result
and	Logical AND	x and y	False
or	Logical OR	x or y	True
not	Logical NOT	not x	False

"""

a=10
b=False
print("Python Logical Operators a and b: ", a and b)

"""
Python Comparison Operators
Operator	Name	        Example (a=10, b=3)	Result
==	    Equal to	                a == b	    False (10 is not equal to 3)
!=	    Not equal to	            a != b	    True (10 is not equal to 3)
>	    Greater than	            a > b	    True (10 is greater than 3)
<	    Less than	                a < b	    False (10 is not less than 3)
>=	    Greater than or equal to	a >= b	    True (10 is greater than 3)
<=	    Less than or equal to	    a <= b	    False (10 is not less than or equal to 3)
"""

a=10
b=20
print("Python Comparison Operators a == b: ", a == b)
