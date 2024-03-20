# Python Code Examples

## Array Operations

### Integer Array
```python
import array as arr

a = arr.array("i", [1, 2, 3, 4, 5, 6])

print("Integer Array")
for i in a:
    print(i)
```

### Float Array
```python
d = arr.array("d", [2.4, 3.5, 6.7, 3.2])

print("Float Array")
for i in d:
    print(i)
```

### Character Array
```python
u = arr.array("u", ['a', 'b', 'c', 'd', 'e', 'f'])

print("Char Array")
for i in u:
    print(i)
```

## FizzBuzz Program

```python
num = int(input("Enter Number\n"))

if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("buzz")
```

## String Operations

### String Case Conversion
```python
s = input("Enter Your full name: ")
print(s.upper())
print(s.lower())
```

### Sentence Manipulation
```python
sent = input("Please enter sentence: ")
sentarray = sent.split(" ")
print(sentarray[0])
print(sentarray)
print(len(sentarray))
```

## Mathematical Operations

### Math Module
```python
import math as mt

print(mt.sin(90))
print(mt.cos(90))
print(mt.sqrt(4))
```

### Numpy Module
```python
import numpy as np

print(np.sin(90))
print(np.cos(90))
print(np.sqrt(4))
```

### Range and Arange
```python
narray=range(10)
narray2=range(1,10)
narray3=range(1,10,2)
print(narray)
print(narray2)
print(narray3)

print("Range(10)")
for i in range(10):
    print(i)
print("Range(1,10)")
for i in (1,10):
    print(i)
print("Range(1,10,2)")
for i in range(1,10,2):
    print(i)

nparray=np.arange(0,np.pi,0.1)
print(nparray)
nparray2=2*nparray
print(nparray2)
```

## File Operations

### Writing to a File
```python
f = open("abc.txt", "w")
f.write("abc\n")
f.close()
```

### Appending to a File
```python
name = input("Enter file name: ")
text = input("Write in file: ")

f = open(name, "w")
f.write(text)
f.close()
```

## Numpy Operations

### Creating and Saving Numpy Array
```python
import numpy as np

nparray = np.arange(0, 10, 1)
num = int(input("Enter Number: "))

nparray2 = num * nparray
print(nparray2)

f = open("file.txt", "w")
result = str(nparray2)
f.write(result)
f.close()
```

## Plotting Graphs

### Using Matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)

plt.xlabel = "X Axis"
plt.ylabel = "Y Axis"
plt.plot(x, y)
plt.show()
```

### Plotting Sin and Cos Graphs Together
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

plt.xlabel = "X Axis"
plt.ylabel = "Y Axis"
plt.plot(x, y)
plt.plot(x, z)
plt.show()
```

### Plotting Tan Graph
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.1)
y = np.tan(x)

plt.xlabel = "X Axis"
plt.ylabel = "Y Axis"
plt.plot(x, y)
plt.show()
```

