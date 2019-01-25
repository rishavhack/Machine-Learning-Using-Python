# Simple Linear Regression

## Regression
 <p>
 	Regression is an analysis of relationship between dependent and independent variables.It is a correlation between two variables.Regression analysis helps to understand how the value of a dependent variable changes when any of the values of independent variable varies.
 </p>

## Types of Regression

Types of regression are as follows :

<ul>
	<li>1. Simple Linear Regression</li>
	<li>2. Multiple Linear Regression</li>
	<li>3. Polynomial Regression</li>
	<li>4. Support Vector for Regression(SVR)</li>
	<li>5. Decision Tree Regression</li>
	<li>6. Random Forest Regression</li>
</ul>


## Simple Linear Regression

> Simple linear regression determines the relationship between dependent and independent variables.It is a statistical analysis which predicts values of dependent variables based on the values of the independent variables.

```
Consider equation of a straight line,
y = c + mx
```
<ul>
	<li>where y is the dependent variable</li>
	<li>c is a constant</li>
	<li>x is independent variable</li>
	<li>m is an coefficient i.e. slope of the line.</li>
</ul>

<p>We are to fit our training dataset into simple linear regression model.To do this create an object regressor of class LinearRegression.  Fit training data i.e. x_train and y_train in regressor as below.</p>

```
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
```

<b>regressor.fit()</b> method takes dependent and independent variables as parameters. We are actually teaching the regressor that y_train values are all corresponding to X_train values.


## Predicting salaries

We are now going to predict the salaries related to X_test values 

```
y_pred = regressor.predict(X_test)
```

<b>regressor.predict()</b> method predicts the values and y_pred values are predicted.we will compare them with y_test.

## Simple Linear Regression Graph:
Training Set

```
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
```

<ul>
	<li>plt.scatter(X_train, y_train , color = 'red') plots scatter graph of salaries against years of experience for values in X_train and y_train</li>
	<li>lt.plot(X_train, regressor.predict(X_train), color = 'blue') plots the graph of predicted salaries against years of experience.</li>
	<li>Red dots represents co-relation between X_train and y_train i.e salaries and years of experience</li>
	<li>Blue line is the simple linear regression.</li>
</ul>

## Test Set:

```
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
```
plt.scatter(X_test, y_test , color = 'red') plots scatter graph of salaries against years of experience for values in X_test and y_test.

>Please note that blue regression line remains the same as it shows all predicted salaries for any years of experience

From the graph and our comparison of y_pred and y_test we can say that we have successfully predicted salaries for any given number of years of experience using Simple Linear Regression using python.


