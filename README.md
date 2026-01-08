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

## Samples

Below is a summary of the specific samples and demonstrations included in each script.

- `basic.py`
  - Hello world and `print()` examples
  - Declaring variables and common types (str, int, float, bool, None)
  - Checking types with `type()`
  - Type conversion (`int()`, `float()`, `str()`)
  - Arithmetic, logical, and comparison operator examples

- `console-input.py`
  - Using `input()` to read user input from the console and printing it

- `file-io.py` (+ `demo-file-io.txt`)
  - Writing files (`w`) and appending (`a`, `a+`)
  - Reading full files with `read()` and partial reads with `read(n)`
  - `readline()` to read single lines
  - Using `with open(...) as f` context manager
  - Explanation of file modes and common functions (`seek`, `tell`, etc.)

- `dictionary-sets.py`
  - Creating and updating dictionaries, nested dictionaries
  - Accessing values with `[]` and `get()`
  - Common dictionary methods (`keys()`, `items()`, `update()`, `pop()`)
  - Creating sets and set operations (`add`, `update`, `remove`, `union`, `intersection`, `difference`)

- `functions.py`
  - Defining functions with `def` and returning values
  - Default parameter values
  - Iterative factorial example
  - Recursive function examples and factorial via recursion

- `if-statement.py`
  - `if`, `elif`, and `else` branching examples

- `list-tuple.py`
  - Creating and modifying lists, indexing, slicing
  - Common list methods (`append`, `insert`, `sort`, `reverse`, `count`)
  - Tuple creation and immutability discussion

- `loops.py`
  - `while` loop (counter and iterating a list)
  - `break` and `continue` examples
  - `for` loop over lists and `for...else` behavior

- `oops.py` (OOP samples)
  - Public and private attributes and methods
  - Static methods and class methods
  - Inheritance: single, multi-level, and multiple inheritance examples
  - `@property` usage and property-like methods
  - Operator overloading demonstration and a small `Bank_Account` demo

- `range.py`
  - Using `range()` with `start`, `stop`, `step` and reverse iteration examples

- `string-function.py`
  - String concatenation, `upper()`, `len()`, indexing and slicing
  - Common string methods (`find`, `replace`, `count`, `startswith`, `endswith`, `split`, `join`, etc.)

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

> _Generated and maintained by GitHub Copilot (Raptor mini, Preview)._