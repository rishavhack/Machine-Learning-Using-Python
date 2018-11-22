#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:09:40 2018

@author: rishav
"""
#Importing libraries
import matplotlib as plt
import numpy as np
from sklearn import datasets,linear_model

#Load dataSet

diabetes = datasets.load_diabetes()

#To check what is in dataSet
print diabetes.keys()
#['data', 'DESCR', 'feature_names', 'target']
print diabetes.data


