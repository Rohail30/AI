# Notes for mids
## Corelation

### Three Parts of code
### One

Data is imported from library and plotted
```python
# correlation example using seaborn
#seaborn is a child library of pyplot
import matplotlib.pyplot as plt
import seaborn as sb

#example of the tips data set available in seaborn python library
dataframe = sb.load_dataset('tips')
sb.pairplot(dataframe, kind="scatter")
plt.show()
```

### Two

Finding corelation using panda
```python
import pandas as pd

x = pd.Series(range(1,20))
y = pd.Series([5,45,88, 3,5,44,9,62,11,50])

print(x.corr(y))
#print(v.corr(x))
```

### Three

Finding corelation using numpy
```python
#Calculating correlation values - numpy

import numpy as np
#x = np.arange(1,11)
x = np.arange(0,10)
y = np.array([5,45,88, 3,5,44, 9,62, 11,50])
find_correlation = np.corrcoef(x,y)

print('Values of x', x)
print('Values of y', y)
print('\n Correlation Coefficient: \n', find_correlation)
# #print('\n Correlation Coefficient: \n', find_correlation[0,1])
```

## Regression


