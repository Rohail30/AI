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
### Four Parts of code
### One
Data is imported from library and plotted with regression line
```python
#regression example using seaborn
import seaborn as sb
from matplotlib import pyplot as plt
dataframe = sb.load_dataset('tips')
sb.regplot(x = "total_bill", y = "tip", data = dataframe)
plt.show()
```
### Two
import data from csv file and normal plotting without regression
```python
import pandas as pd
import numpy as np
from sklearn import linear_model #scikit Learn python Library, using Linear_model for Linear regression python modeL
import matplotlib.pyplot as plt
#Loading data
dataframe = pd.read_csv("homeprices.csv")
dataframe
#for displaying distribution of datapoints, using scatter plot
#%matplotlib inline
plt.xlabel('area(sq. ft)')
plt.ylabel('price($)')
plt.scatter(dataframe.area, dataframe.price, color='green', marker='.')
```
### Three
predicted and other regresion values
```python
#creating object for Linear regression model
linear_Reg_Obj = linear_model.LinearRegression()

#training Linear regression model using available datapoints
linear_Reg_Obj.fit(dataframe[['area']], dataframe.price) #passign arguments to 2D array

#predicting price
#by calculating cooefficient and intercept
#Predicted value
linear_Reg_Obj.predict([[4500]])

#displaying value of coefficient
linear_Reg_Obj.coef_

#displaying value of y intercept
linear_Reg_Obj.intercept_

#Actual Value
#understanding through Linear equation y=mx+b
#here the equation become y=m*area+b i-e y=coef*area+intercept

135.78767123*4500+180616.43835616432
#which is same as linear_Reg_Obj.predict(4500)
```
### Four
Plotting Regression
```python
#Plotting regression Line
plt.xlabel('area(Sq. ft)', fontsize= 15)
plt.ylabel('price($)', fontsize= 15)
plt.scatter(dataframe.area, dataframe.price, color='green', marker='.')
plt.plot(dataframe.area, linear_Reg_Obj.predict(dataframe[['area']]), color='blue')
```


