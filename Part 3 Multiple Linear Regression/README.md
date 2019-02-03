# Multiple Linear Regression
<p>
	Multiple linear regression is similar to simple linear regression.In simple linear regression we had only one dependent and one independent variable whereas, in multiple linear regression we will teach machine to predict the values of dependent variable from two or more independent variables.
</p>

Mathematical equation of multiple linear regression:
```
y = b1X1+b2X2+b3X3+….+bnXn
```
<ul>
	<li>y is dependent variable</li>
	<li>b1,b2… are constants</li>
	<li>X1,X2… are independent variables</li>
</ul>

## Dummy Variables

When we encode the categorical data,skLearn library in Python creates separate column for each categorical data.So,when we encode this data,we get separate column created for all three categories.

### Suppose
<table>
  <tr>
    <th>Development</th>
    <th>Testing</th>
    <th>UX</th>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>1</td>
  </tr>
</table>


While implementing multiple linear regression we will eliminate one dummy variable.For example,in the first row development = 1, testing = 0 and UX = 0.Each row should contain value one in only one of the column.So consider the first row


<ul>
	<li>If we remove development column then testing and UX are 0 which mean development should be 1</li>
	<li>If we remove testing column,development is already 1 and all the other columns should be 0</li>
	<li>If we remove UX column,development is already 1 and all the other columns should be 0</li>
</ul>


## Multiple Linear Regression Implementation


```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
# Importing the dataset
dataset = pd.read_csv('Employee_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
 
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
 
# Avoiding the Dummy Variable Trap
X = X[:, 1:]
 
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
 
# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
 
# Predicting the Test set results
y_pred = regressor.predict(X_test)
```

In above code snippet we have used data preprocessing template and after splitting dataset into train and test.we have used LinearRegression class from sklearn.linear_model library exactly same as we used in simple linear regression.After executing the above code we will have predicted values for X_test in y_pred that is y_pred will have salaries predicted from the data available in X_test.

# Backward Elimination For Multiple Regression

We learned about multiple linear regression and predicted values of dependent variables based on multiple independent variables. However how can we identify the impact made by a specific independent variable on dependent variable? We can follow backward elimination for multiple linear regression to identify independent variables which have most impact on dependent variables.

