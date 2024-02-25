### Data Types Examples

- **int:** Example: 3, 2  
- **float:** Example: 2.5, 3.5 
- **string:** Example: "Wali", "Muhammad"
- **bool:** Example: True, False
- **list:** Example: [2, 4, "Wali", 3.5, 6.5, "Muhammad"]
- **tuple:** Example: (2, 4, "Wali", 3.5, 6.5, "Muhammad")
- **dictionary:** Example: {"Name": "Wali", "Gender": "Male", "Age": "26"}

# Variables and Data Types

```python
x = 3
y = 2.5
z = "Wali"

print("Value of x is ", x)
print("Value of x is ", y)
print("Value of x is ", z)

print("the type of x is ", type(x))
print("the type of x is ", type(y))
print("the type of x is ", type(z))
```

# User Input

```python
print("please enter your name")
name = input()
print("Your name is ", name)

print("Please enter your age")
age = input()
a = int(age)
print(type(age))
print(type(a))

val1 = int(input("Enter Value: "))
val2 = int(input("Enter another Value: "))
print("the sum of entered values is ", (val1 + val2))
print("the product of entered values is ", (val1 * val2))
print("the difference of entered values is ", (val1 * val2))
```

# Slicing

```python
name = input("Enter Name: ")
n = name[0:3]
m = name[0:]
o = name[:4]
p = name[:]

print(m)
print(n)
print(o)
print(p)
```

# Arrays and Lists

```python
listt = [2, 4, "Wali", 3.5, 6.5, "Muhammad"]
for i in listt:
    print(i)

print(" ")
print(len(listt))
print(" ")

sublist = listt[2:5]
for i in sublist:
    print(i)

print(" ")

sublist = listt[:5]
for i in sublist:
    print(i)

print(" ")

sublist = listt[2:]
for i in sublist:
    print(i)

print(" ")

sublist = listt[:]
for i in sublist:
    print(i)
```

# Tuples

```python
tup = (2, 4, "Wali", 3.5, 6.5, "Muhammad")
for i in tup:
    print(i)

print(" ")
print(len(tup))
print(" ")

sublist = tup[2:5]
for i in sublist:
    print(i)

print(" ")

sublist = tup[:5]
for i in sublist:
    print(i)

print(" ")

sublist = tup[2:]
for i in sublist:
    print(i)

print(" ")

sublist = tup[:]
for i in sublist:
    print(i)
```

# Class Task

```python
n = int(input("Enter a number: "))
if n % 3 == 0:
    print("fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print("Nothing")
```

# Dictionaries

```python
person = {"Name": "Wali", "Gender": "Male", "Age": "26"}
print(person.keys())
print(person.values())
print("Person's name is", person["Name"])
```

# Task 1
Write a program that takes input from the user and print it's table using list.Should only be even

```python
# Take input from the user
num = int(input("Enter a number: "))

# Create a list to store the table
table = []

# Calculate and store the table for even numbers
for i in range(2, 11, 2):
    table.append(num * i)

# Print the table
print("Table for", num, "using even numbers:")
for i, val in enumerate(table, start=2):
    print(num, "*", i, "=", val)
```

# Task 2
Task2 : Write a program that defines a person dictionary with the following keys 
- Name
- Age
- Gender
- Program
- University
- All the values should be assigned by user input

```python
n = input("Enter name: ")
a = int(input("Enter age: "))
g = input("Enter Gender: ")
p = input("Enter Program: ")
u = input("Enter University: ")

d = {}

d["Name"] = n
d["age"] = a
d["Gender"] = g
d["Program"] = p
d["University"] = u

print(d)
```

