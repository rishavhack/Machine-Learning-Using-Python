#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:29:19 2018

@author: rishav
"""
import spacy
import numpy as np
import pandas as pd
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

pd.Series(data = my_data)
pd.Series(data=my_data,index=labels)
pd.Series(my_data,labels)
pd.Series(arr)
pd.Series(arr,labels)
pd.Series(d)
pd.Series(data=labels)
ser1 = pd.Series([1,2,3,4],['USA','Germany','UK','India'])
ser2 = pd.Series([1,2,5,4],['USA','Germany','UK','India'])