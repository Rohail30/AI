## Depth First Search (DFS)

### Generating Adjacency List for Undirected Graph

```python
from collections import defaultdict

# Generate adjacency List for undirected graph
def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList

# Define the edges of the graph
edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'],
         ['C', 'F'], ['C', 'G'], ['D', 'H'], ['D', 'I'],
         ['E', 'J'], ['E', 'K'], ['F', 'L'], ['F', 'M']]

# Generate the adjacency list
adjacencyList = generateAdjacencyLst(edges)

# Output the adjacency list
print(adjacencyList)
```

### Depth First Search (DFS) Traversal

```python
# find dfs traversal from starting vertex
def dfs(adjacencyList, vertex, visitedSet = None, path = None) :
    # create memo once in top-Level call
    if visitedSet is None:
        visitedSet = set() # empty set
    if path is None:
        path = [] # empty list

    visitedSet.add(vertex) # A is added to the visited set
    path.append(vertex) # A is added to the path list
    if vertex in adjacencyList: # true 
        for neighbor in adjacencyList[vertex]: # iterate the adjacency list for B and C as neighbor values
            if neighbor not in visitedSet: # B and C are not in visited list yet so true
                dfs(adjacencyList, neighbor, visitedSet, path) # recursive call and now vertex is B
    return path

print(dfs(adjacencyList, 'A')) # Output: ['A', 'B', 'D', 'H', 'I', 'E', 'J', 'K', 'C', 'F', 'L', 'M', 'G']
```

### Depth First Search (DFS) Traversal with Multiples of Two

```python
# Define the edges of the graph with multiples of two
edges = [['2', '4'], ['2', '6'], ['4', '8'], ['4', '10'], 
         ['6', '12'], ['6', '14'], ['8', '16'], ['8', '18'], 
         ['10', '20'], ['10', '22'], ['12', '24'], ['12', '26']]

# Generate the adjacency list
adjacencyList = generateAdjacencyLst(edges)

print(dfs(adjacencyList, '2')) # Output: ['2', '4', '8', '16', '18', '10', '20', '22', '6', '12', '24', '26', '14']
```

## Correlation

### Correlation Example Using Seaborn

```python
# correlation example using seaborn
import matplotlib.pyplot as plt
import seaborn as sb

# Example of the tips data set available in seaborn python library
dataframe = sb.load_dataset('tips')
sb.pairplot(dataframe, kind="scatter")
plt.show()
```

### Calculating Correlation Values - Pandas

```python
import pandas as pd

x = pd.Series(range(1,20))
y = pd.Series([5,45,88, 3,5,44,9,62,11,50])

print(x.corr(y)) # Output: 0.058065327411248945
```

### Calculating Correlation Values - NumPy

```python
import numpy as np

x = np.arange(0,10)
y = np.array([5,45,88, 3,5,44, 9,62, 11,50])

find_correlation = np.corrcoef(x,y)

print('Values of x', x)
print('Values of y', y)
print('\n Correlation Coefficient: \n', find_correlation)
```

## Regression

### Regression Example Using Seaborn

```python
# regression example using seaborn
import seaborn as sb
from matplotlib import pyplot as plt

dataframe = sb.load_dataset('tips')
sb.regplot(x = "total_bill", y = "tip", data = dataframe)
plt.show()
```

