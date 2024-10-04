# -*- coding: utf-8 -*-
"""assignment2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15RRvROaWc5vpPcCJ_3EpB9lU0i8vIgez
"""

import pandas as pd
import numpy as np
import patsy as pt

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from xgboost import XGBClassifier

training = pd.read_csv("https://github.com/dustywhite7/Econ8310/raw/master/AssignmentData/assignment3.csv")

#training = training.drop('DateTime', axis = 'columns')
training['DateTime'] = pd.to_datetime(training['DateTime'])

training["day"] = training['DateTime'].map(lambda x: x.day)
training["month"] = training['DateTime'].map(lambda x: x.month)
training["year"] = training['DateTime'].map(lambda x: x.year)
training["hour"] = training['DateTime'].map(lambda x: x.hour)

training = training.drop('id', axis = 'columns')
training = training.drop('DateTime', axis = 'columns')

Y = training['meal']
X = training.drop('meal', axis = 'columns')

model = DecisionTreeClassifier(max_depth=20, min_samples_leaf=10)

modelFit = model.fit(X,Y)

testData = pd.read_csv("https://github.com/dustywhite7/Econ8310/raw/master/AssignmentData/assignment3test.csv")

testData['DateTime'] = pd.to_datetime(testData['DateTime'])

testData["day"] = testData['DateTime'].map(lambda x: x.day)
testData["month"] = testData['DateTime'].map(lambda x: x.month)
testData["year"] = testData['DateTime'].map(lambda x: x.year)
testData["hour"] = testData['DateTime'].map(lambda x: x.hour)

testData = testData.drop('id', axis = 'columns')
testData = testData.drop('DateTime', axis = 'columns')
Xt = testData.drop('meal', axis = 'columns')

pred = model.predict(Xt)