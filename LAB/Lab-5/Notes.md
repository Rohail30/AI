# Notes for mids
## KNN

### Nine Parts of code
### One
Importing dataset iris_dataset which is dictionary of key-value pairs 
```python
import pandas as pd
from sklearn.datasets import load_iris
iris_dataset = load_iris() # loading iris dataset using sklearn
iris_dataset.feature_names
iris_dataset.target_names
```
### Two
making new dataset of .data values using panda library and also giving heading for column of feature's name
```python
df = pd.DataFrame(iris_dataset.data, columns=iris_dataset.feature_names)
df.head()
```
### Three
Adding target and Flower Name column and setting flower name to its corresponding value
```python
df['target']=iris_dataset.target
df['flower_name']=df.target.apply(lambda x: iris_dataset.target_names[x])
df.head()
```
### Four
display data containing target value 1
```python
df[df.target==1].head() #display data containing target value 1
# df[df.target==2].head() # display data containing targer value 2
```
### Five
different length of display
```python
df0=df[:50]
df1=df[50:100]
df2=df[100:]
```
### Six
Plotting
```python
import matplotlib.pyplot as plt
%matplotlib inline

#Sepal Length vs Sepal Width (Setosa vs Versicolor)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'],color="green",marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'],color="blue",marker='.')
```
### Seven
Training
```python
#Creating traning and testing dataframe
#Train test split

from sklearn.model_selection import train_test_split
X = df.drop(['target', 'flower_name'], axis='columns')
y = df.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
len(X_train)
len(X_test)
#creating KNN ( K neearest neighbor Classifier)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train) # Learning and prediction
```
### Eight
Predicting
```python
knn.score(X_test, y_test) #check prediction/performance score
#knn.predict([[4.8,3.0,1.5,0.3]]) #passing test values to predict the species
predicted_value = knn.predict([[6.5,2.8,4.6,1.5]]) #passing test values to predict the species

print('KNN Species Prediction:', predicted_value)
```
### Nine
Plotting Prediction
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



