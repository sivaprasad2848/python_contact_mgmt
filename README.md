
# PYTHON PROGRAMMING – COMPLETE SHORT NOTES

## 1. Variables
A variable is a named memory location used to store data.

```python
name = "Munna"
age = 21
```

## 2. Data Types
Data types define the type of data stored in a variable.

- `int` – Integer numbers (10, 20)
- `float` – Decimal numbers (10.5)
- `str` – String or text ("Python")
- `bool` – Boolean values (True, False)
- `list` – Ordered and mutable collection.
- `tuple` – Ordered and immutable collection.
- `dict` – Key-value pair collection.
- `set` – Collection of unique elements.

**Type checking:**
```python
print(type(name))
```

## 3. Input and Output

- `input()` – Gets input from the user.
- `print()` – Displays output on the screen.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)
```

**Type conversion:**
- `int()` – Converts into integer.
- `float()` – Converts into decimal.
- `str()` – Converts into string.

## 4. Operators
Operators are symbols used to perform operations on variables and values.

| Type | Operators |
|---|---|
| Arithmetic | `+`, `-`, `*`, `/`, `%`, `//`, `**` |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Logical | `and`, `or`, `not` |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=` |
| Membership | `in`, `not in` |

**Modulus (`%`):** Returns the remainder of division. It is commonly used for odd/even checking.

## 5. Conditional Statements
Conditional statements are used to execute code based on conditions.

- `if` – Executes when the condition is true.
- `elif` – Checks another condition.
- `else` – Executes when all conditions are false.

```python
if a > b:
    print("A is greater")
elif a == b:
    print("Both are equal")
else:
    print("B is greater")
```

## 6. Odd or Even
A number is even if it is divisible by 2. Otherwise, it is odd.

```python
a = int(input("Enter a number"))

if a % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

## 7. Multiple If Statements
Multiple independent `if` statements are used to check multiple conditions separately.

**Example: Day checking**

```python
day = int(input("Enter a day"))

if day == 1:
    print("Sunday")
if day == 2:
    print("Monday")
if day == 3:
    print("Tuesday")
if day == 4:
    print("Wednesday")
if day == 5:
    print("Thursday")
if day == 6:
    print("Friday")
if day == 7:
    print("Saturday")
if day > 7 or day < 1:
    print("Invalid Day")
```

**Note:** Unlike `elif`, multiple `if` statements can execute independently.

## 8. Loops
Loops are used to execute a block of code repeatedly.

**Types:**

1. `for` loop – Iterates through a sequence.
2. `while` loop – Executes while a condition is true.
3. Nested loop – A loop inside another loop.

### While Loop

```python
i = 0
while i < 10:
    print(i)
    i = i + 1
```

### For Loop

```python
products = ['apple', 'orange', 'mango']

for item in products:
    print(item)
```

## 9. Nested Loops
A nested loop is a loop placed inside another loop. The inner loop executes completely for each iteration of the outer loop.

```python
i = 1
while i < 8:
    j = 1
    while j < 10:
        res = i * j
        print(str(i) + "*" + str(j) + "=" + str(res))
        j = j + 1
    i = i + 1
```

## 10. Loop Control Statements
Loop control statements change the normal execution of loops.

- `break` – Terminates the loop immediately.
- `continue` – Skips the current iteration and moves to the next iteration.
- `pass` – Does nothing; used as a placeholder.

**Example: Continue**

```python
i = 1
while i < 10:
    if i == 3:
        i = i + 1
        continue
    print(i)
    i = i + 1
```

## 11. Lists
A list is an ordered and mutable collection used to store multiple values in a single variable.

**Features:**
- Allows duplicate values.
- Supports different data types.
- Uses indexing starting from 0.
- Elements can be added, updated and deleted.

**Example:**

```python
products = ['apple', 'orange', 'mango']
```

**List methods:**

| Method | Purpose |
|---|---|
| `append()` | Adds an element at the end |
| `insert()` | Adds an element at a specific index |
| `remove()` | Removes an element by value |
| `pop()` | Removes and returns an element |
| `len()` | Returns the number of elements |
| `del` | Deletes an element using its index |

## 12. Tuples
A tuple is an ordered and immutable collection used to store multiple values.

**Features:**
- Allows duplicate values.
- Supports different data types.
- Uses indexing.
- Elements cannot be directly modified.

**Example:**

```python
contact = ('sam', 'sam@gmail.com', 8728378)
```

**Accessing tuple elements:**

```python
print(contact[0])
print(contact[1])
print(contact[2])
```

## 13. Strings
A string is a sequence of characters enclosed within single, double or triple quotes.

**String operations:**
- Concatenation – Joining strings using `+`.
- Repetition – Repeating strings using `*`.
- Indexing – Accessing individual characters.
- Slicing – Extracting part of a string.

```python
name = "Python"
print(name[0])
```

**String conversion:**

```python
mobile = 9876543210
print(str(mobile))
```

## 14. Functions
A function is a reusable block of code designed to perform a specific task.

**Syntax:**

```python
def function_name():
    statements
```

**Types:**
- Built-in functions – `print()`, `input()`, `len()`.
- User-defined functions – Created using the `def` keyword.

**Example:**

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

**Important terms:**
- Parameter – Variable declared in a function.
- Argument – Value passed to a function.
- Return – Sends a result back from a function.

## 15. File Handling
File handling is the process of creating, reading, writing and modifying files using Python. It helps store data permanently.

### File Operations

1. Create – Creates a new file.
2. Read – Reads file contents.
3. Write – Writes data into a file.
4. Append – Adds data at the end of a file.
5. Close – Closes an opened file.

### Opening a File

The `open()` function is used to open a file.

**Syntax:**

```python
fp = open("data.txt", "mode")
```

### File Modes

| Mode | Description |
|---|---|
| `r` | Read mode |
| `w` | Write mode; overwrites existing content |
| `a` | Append mode |
| `x` | Creates a new file |
| `r+` | Read and write mode |

### Writing into a File

The `write()` function is used to write data into a file.

```python
fp = open("data.txt", "w")
fp.write("Hello Python")
fp.close()
```

### Reading a File

The `read()` function reads the contents of a file.

```python
fp = open("data.txt", "r")
data = fp.read()
print(data)
fp.close()
```

### Appending Data

The append mode adds new data without deleting the existing contents.

```python
fp = open("data.txt", "a")
fp.write("Welcome Python\n")
fp.close()
```

### File Handling Functions

| Function | Purpose |
|---|---|
| `open()` | Opens a file |
| `read()` | Reads entire content |
| `readline()` | Reads one line |
| `readlines()` | Reads all lines into a list |
| `write()` | Writes data |
| `writelines()` | Writes multiple strings |
| `close()` | Closes the file |
| `tell()` | Returns current file pointer position |
| `seek()` | Changes file pointer position |

### File Pointer

A file pointer indicates the current position in a file.

- `tell()` – Returns the current position.
- `seek()` – Moves the pointer to a specified position.

### Newline Character

`\n` is used to move the next content to a new line.

```python
fp.write("Apple\n")
fp.write("Orange\n")
```

## 16. Contact Management Program – Concepts

The contact management program uses the following Python concepts:

1. Variable – Stores menu options and contact information.
2. List – Stores multiple contacts.
3. Tuple – Stores individual contact details.
4. While loop – Repeats the menu until the user exits.
5. Conditional statements – Selects the required operation.
6. Input – Gets name, email and mobile number.
7. Append – Inserts a new contact.
8. For loop – Displays all contacts.
9. Indexing – Accesses individual contact details.
10. Delete – Removes a contact using its index.
11. Update – Replaces an existing contact.
12. Function – Organizes reusable operations.
13. File handling – Saves contact details permanently.

### Contact Operations

| Operation | Python syntax |
|---|---|
| Insert | `contact.append((name,email,mobile))` |
| Display | `for contacts in contact:` |
| Access | `contacts[0]` |
| Delete | `del contact[i]` |
| Update | `contact[i] = (name,email,mobile)` |

## 17. Writing Data into a File Using Function

A user-defined function can be used to save multiple contacts into a text file.

```python
def write_to_file(c):
    fp = open("data.txt", "a")
    for item in c:
        data = item[0] + " " + item[1] + " " + str(item[2]) + "\n"
        fp.write(data)
    fp.close()

contacts = [
    ('sam', 'sam@gmail.com', 8728378),
    ('thaswin', 'thaswin@gmail.com', 800008),
    ('rihan', 'rihan@gmail.com', 8888888)
]

write_to_file(contacts)
```

**Explanation:**

- `def` – Defines a function.
- `write_to_file(c)` – Function that accepts contacts.
- `open()` – Opens the file in append mode.
- `for` – Iterates through the contact list.
- `item[0]` – Accesses the name.
- `item[1]` – Accesses the email.
- `item[2]` – Accesses the mobile number.
- `str()` – Converts mobile number into a string.
- `\n` – Moves data to a new line.
- `write()` – Writes data into the file.
- `close()` – Closes the file.

## 18. Comments
Comments are used to explain the source code. Python ignores comments during execution.

**Types:**
- Single-line comment – Starts with `#`.
- Multi-line comments – Commonly written using multiple `#` lines.
- Docstring – Documentation string written using triple quotes.

```python
# This is a comment
```

# OOPS

it is a programming methodology which is used for real world programming

Features of OOP

1) Class
	->core concept of OOP
	->a class is a collection of properties/variables and methods/functions

	->syntax:
		
		class <class-name>
			properties
			methods
		eg:
			class vehicle:
				no_of_tyres=0
				fuel_type=none
				def set_data(self):
					self.no_of_tyres=4
					self.fuel_typre="Petrol"
				def display(self):
					print(self.no_of_tyres)
					print(self.fuel_type)
2. Object
	-> if you want to use a class you need create object
	-> object is a copy of class
	->syntax:-
		
-----------------------------------------------------------------
def __init__(self):
	print("This is constructor")
def __del__(self):
	print("This is destrcutor")

constructor used for printing or using on starting of code
destructor used for printing or using on ending of code
------------------------------------------------------------------
3. Encapsulation:
	->





----------------------------------------------------------

TKinter

GUI for python
Graphical User Interface

---------------------
Inheritance

Acquiring the features of one class to another inheritance

Types of Inheritance:-
 - single
 - multiple
 - multilevel
 - hierarchichal
 - hybrid