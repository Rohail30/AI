# Iris Dataset Analysis

## Loading Dataset and Basic Exploration

```python
import pandas as pd
from sklearn.datasets import load_iris

iris_dataset = load_iris()  # loading iris dataset using sklearn
iris_dataset.feature_names
```

```python
iris_dataset.target_names
```

```python
df = pd.DataFrame(iris_dataset.data, columns=iris_dataset.feature_names)
df.head()
```

## Adding Target and Flower Name Columns

```python
df['target'] = iris_dataset.target
df.head()
```

```python
df['flower_name'] = df.target.apply(lambda x: iris_dataset.target_names[x])
df.head(10)
```

```python
df[45:55] #checking range of target values
```

```python
df0=df[:50]
df1=df[50:100]
df2=df[100:]
import matplotlib.pyplot as plt
%matplotlib inline

#Sepal Length vs Sepal Width (Setosa vs Versicolor)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'],color="green",marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'],color="blue",marker='.')
```

```python
#Petal Length vs Pepal Width (Setosa vs Versicolor)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.scatter(df0['petal length (cm)'], df0['petal width (cm)'], color="green",marker='+')
plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'], color="blue", marker='.')
```

```python
#Creating traning and testing dataframe
#Train test split

from sklearn.model_selection import train_test_split
X = df.drop(['target', 'flower_name'], axis='columns')
y = df.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
len(X_train)
```

```python
len(X_test)
```

```python
#creating KNN ( K neearest neighbor Classifier)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train) # Learning and prediction
```

```python
knn.score(X_test, y_test) #check prediction/performance score
```

```python
#knn.predict([[4.8,3.0,1.5,0.3]]) #passing test values to predict the species
predicted_value = knn.predict([[6.5,2.8,4.6,1.5]]) #passing test values to predict the species

print('KNN Species Prediction:', predicted_value)
```

```python
#Plotting Confusion Matrix
from sklearn.metrics import confusion_matrix
y_pred = knn.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
cm
```

```python
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sn
plt.figure(figsize=(10,5))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted', fontsize = 15)
plt.ylabel('Truth', fontsize = 15)
```

```python
#Generating classification report for precesion, recall and f1-score for each classes

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```
