# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#First Program
Lohit = 12
Lohit
Lohit2 = "SM"
Lohit3 = "12"
Lohit2 + " " + Lohit3

type(Lohit)
type(Lohit2)
type(Lohit3)

Lohit4 = True
type(Lohit4)
help(str)

help(LinearRegression)
Lohit5 = [1,2,3,4,5]
Lohit5 
type(Lohit5)
Lohit5 + Lohit5
Lohit6 = [Lohit5, [Lohit5], Lohit2]
Lohit6
type(Lohit6)


import numpy as np  #to convert in to Array
import pandas as pd   # used for data file oprations.
import matplotlib.pyplot as plt  #to plot Graphs
import sklearn as sklearn
import seaborn as sb
Lohit7 = np.array(Lohit5)
Lohit7
Lohit7 + Lohit7



# IMportng the data
import pandas as pd
file = pd.read_csv('E:/PytonExercise/issuelist.csv')
file = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')


# Naming the column
file.columns= ["Iris1", "Iris2", "Iris3", "Iris4","Iris5"]

# seeing the type of data
file.dtypes

#seeing types of data under each column
type(file)
type(Iris1)
type(file.Iris1)
type(file.Iris2)
type(file.Iris3)
type(file.Iris4)
type(file.Iris5)


#seeing types of data under each column in another way.
type(file["Iris1"])

file.loc[0]
file.loc[1]
# finding data based on the index
file.loc[1][2]


file.loc[[1:3],[3]]

file.iloc[3]

file.iloc[1:2,2:3]
file.iloc[1:3,2:3]
file.iloc[0,2]

file.iloc[0:1,2]

file.iloc[0:2,2]

file.iloc[0,0:1]

file.iloc[0,0:2]

file.iloc[0:5,0:2]

file.head()

file.tail()

file.tail(10)

file.head(10)

file.describe()

sb.pairplot(file)

plt.scatter(file.Iris1,file.Iris2)
plt.scatter(file.Iris1,file.Iris3)
plt.scatter(file.Iris1,file.Iris4)
plt.scatter(file.Iris2,file.Iris2)

plt.hist(file.Iris1)

file.Iris1.mean()
file.Iris1.median()
file.Iris1.mode()
file.corr()

# index iloc : give the index of the location - column and row number
# for location: need to give the labels of rows and columns, for e.g. 7 and Iris4



file.iloc[0,]
file.iloc[0:2,2]
file.iloc[0:2,0:2]
file.iloc[:2,0:2]
file.iloc[0:, 0:2]
file.iloc[0:2,:2]
file.iloc[0:2,0:]

#alternates
file.iloc[[5,12,15,18],[2,4]]


#Sorting
file.groupby("Iris3")

#Subset
subset = file.copy()
subset2 = file.iloc[0:4,1:3]
subset2.to_excel("E:/PytonExercise/toexcel.xlsx")
subset.to_excel("E:/PytonExercise/toexcel.xlsx")

#Statements
statement = "this is my Python class"
statement.capitalize()
statement.lower()
statement.upper()
statement[0]
statement[0:5]
statement+statement
statement+" "+ statement
statement1 = "My name is Lohit"
statement2 = "I stay in JP Nagar"
statement1 + " and " + statement2

