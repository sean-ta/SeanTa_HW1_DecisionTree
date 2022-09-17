#!/usr/bin/env python
# coding: utf-8

# In[119]:


#-------------------------------------------------------------------------
# AUTHOR: Sean Ta
# FILENAME: SeanTa_decision_tree.py
# SPECIFICATION: Create a decision tree based on contact lens data
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here

X_dict = {'Young':1 , 'Presbyopic':2, 'Prepresbyopic':3,
          'Myope':1, 'Hypermetrope':2,
          'No':1, 'Yes' :2,
          'Reduced':1, 'Normal' :2} # dictionary to map values to numbers

for row in db:
    X.append(row[:-1]) # X is now a list that only contains the categorical training features

for key, val in X_dict.items():
    for row in X:
        if key not in row: # if key does not exist in row, keep going
            continue
        i = row.index(key)
        row[i] = val # set row[i] to value
        

#transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =

Y_dict = {"Yes":1, 
          "No":2} # dictionary to map classes to numbers

for row in db:
    Y.append(row[-1]) # Y is now a list that only contains the classes
    
Y = [x if x not in Y_dict else Y_dict[x] for x in Y] # replace yes and no with value in dictionary


#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy', )
clf = clf.fit(X, Y)

# #plotting the decision tree
plt.figure(figsize=(10,10))
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()


# In[ ]:




