# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 21:04:11 2018

@author: Rishav
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Importing the dataset
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

#For missing value we will give mean value
from sklearn.preprocessing import Imputer
#Create object 
imputer = Imputer(missing_values='NaN',strategy = 'mean',axis = 0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

#We encode name into number
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()


labelencoder_y = LabelEncoder()
y = labelencoder_X.fit_transform(y)

#Splitting the dataset into training sete and Test set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)