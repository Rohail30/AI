# Python Code Examples

## Writing Dictionary to File

```python
reg = int(input("Enter Registration Number: "))
name = input("Enter Name: ")
num = int(input("Enter Number: "))
email = input("Enter Email: ")
uni = input("Enter University: ")
year = int(input("Enter Year: "))

person = {}

person["Registration"] = reg
person["Name"] = name
person["Phone"] = num
person["email"] = email
person["University"] = uni
person["Year"] = year

result = str(person)

f = open("regno.txt", "w")
f.write(result)
f.close()
```

## Drawing Sin and Cos Curves

```python
import matplotlib.pyplot as plt
import numpy as np

xstart = int(input("Enter starting point: "))
xend = int(input("Enter ending point: "))
xincrement = float(input("Enter incremented value: "))

x = np.arange(xstart, xend, xincrement)
y = np.sin(x)
z = np.cos(x)

plt.xlabel = "X Axis"
plt.ylabel = "Y Axis"
plt.plot(x, y)
plt.plot(x, z)
plt.show()
```

## Subplot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
plt.subplot(2, 1, 1)
plt.xlabel = "X Axis"
plt.ylabel = "Y Axis"
plt.grid()
plt.plot(x, y, "g")

y = np.cos(x)
plt.subplot(2, 1, 2)
plt.xlabel = "X Axis"
plt.ylabel = "Y Axis"
plt.grid()
plt.plot(x, y, "r")
plt.show()
```

## Breadth-First Search (BFS)

```python
from collections import defaultdict

def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList

edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G'], ['D', 'H'], ['D', 'I'], ['E', 'J'], ['E', 'K'], ['F', 'L'], ['F', 'M']]
adjacencyList = generateAdjacencyLst(edges)

def bfs(adjacencyList, vertex):
    visitedSet = set()
    queue = []
    visitedSet.add(vertex)
    queue.append(vertex)

    result = []
    while queue:
        v = queue[0]
        result.append(v)
        queue = queue[1:]
        for neighbor in adjacencyList[v]:
            if neighbor not in visitedSet:
                visitedSet.add(neighbor)
                queue.append(neighbor)
    return result

bfs(adjacencyList, 'A')
```

## Depth-First Search (DFS)

```python
from collections import defaultdict

def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList

edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G'], ['D', 'H'], ['D', 'I'], ['E', 'J'], ['E', 'K'], ['F', 'L'], ['F', 'M']]
adjacencyList = generateAdjacencyLst(edges)

def dfs(adjacencyList, vertex, visitedSet = None, path = None) :
    if visitedSet is None:
        visitedSet = set()
    if path is None:
        path = []

    visitedSet.add(vertex)
    path.append(vertex)
    if vertex in adjacencyList:
        for neighbor in adjacencyList[vertex]:
            if neighbor not in visitedSet:
                dfs(adjacencyList, neighbor, visitedSet, path)
    return path

dfs(adjacencyList, 'A')

