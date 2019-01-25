# Data Preprocessing

## Importing Libraries

<ul>
	<li>numpy</li>
	<li>matplotlib</li>
	<li>pandas</li>
</ul>

<p>Using these libraries we are going to read our dataset for data preprocessing.</p>

## Handle Missing Data In Python

<p>In our dataset you can see there are two missing values.To handle these missing values Python uses sklearn library.How does this library handles missing data?In python,to handle missing data mean of all the other values present in that column is calculated.For example,the missing value from the column age will get calculated from the average of other age values present in the same column.</p>

```
from sklearn.preprocessing import Imputer

imputer = Imputer (missing_values= 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(x[:,1:3])
```

<p>In above code snippet you can see we used sklearn.preprocessing library. Imputer is a class present in sklearn library which handles missing values from a dataset.

We have created an object of Imputer class as imputer.This class has many attributes to handle missing values.</p>


## Encode Categorical Data

<p>Categorical data is data which have categories.As machine learnign models are based on mathematical equations,it will be difficult to a machine to read the text values.Hence,we need to encode the categorical data in our dataset.</p>
<br>
<p>For this the same library from missing values i.e.sklearn will be used for encoding categorical data.Following is code snippet</p>

```
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
x[:, 0] = labelEncoder_X.fit_transform(x[:, 0])
oneHotEncoder = OneHotEncoder(categorical_features=[0])
x = oneHotEncoder.fit_transform(x).toarray()
labelEncoder_Y = LabelEncoder()
y = labelEncoder_Y.fit_transform(y)
```


We have used following classes to encode categorical data:

<ul>
	<li><b>LabelEncoder : </b>Encode labels with values between 0 and n-1 i.e [size of array] – 1. </li>
	<li><b>OneHotEncoder : </b>Encode categorical integer features using a one-hot aka one-of-K scheme.</li>
</ul>

## Split Dataset Into Train and Test

<p>We will split dataset into train and test dataset for machine learning models we are going to build in future.Splinting the data into two parts i.e. Train and Test so that the test data we can use to test the machine learning model and train data will be the training data for machine learning model.

To split the dataset we have again used the same library i.e sklearn.We have used train_test_split class which splits some % data into train and test.The best practice is to split 20% of your dataset into test data.</p>

```
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
```
<p>This will split the dataset into Train and 20% test dataset i.e.The Test dataset will have 2 records from our dataset.We have done data preprocessing for upcoming machine learning article series. </p>

<ul>
	<li>x_train : training data of independent variables.</li>
	<li>x_test : test data for which we want to predict </li>
	<li>y_train : training data o dependent variable</li>
	<li>y_test : Actual Result</li>
</ul>