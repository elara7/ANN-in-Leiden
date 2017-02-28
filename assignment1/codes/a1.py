# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:14:35 2017

@author: xmhy_
"""

import numpy as np
import matplotlib.pyplot as plt  
import pandas as pd
import os
os.chdir('C:\\Users\\xmhy_\\Desktop\\NN')

train_in = pd.read_csv('train_in.csv', sep=',',header=None)
train_out = pd.read_csv('train_out.csv', sep=',',header=None)
test_in = pd.read_csv('test_in.csv', sep=',',header=None)
test_out = pd.read_csv('tets_out.csv', sep=',',header=None)

# Inspect the data
train_in.head()
train_out.head()
test_in.head()
test_out.head()

# Prepare the data
train = pd.concat([train_out, train_in], axis = 1)
train.columns = range(0, 257)

test = pd.concat([test_out, test_in], axis = 1)
test.columns = range(0, 257)

##########
# Task 1 #
##########
ts1 = train.groupby(train_out[0])

# Calculate the centroid of the 10 classes.
centroids = train.groupby(train_out[0]).mean()

# Calculate the radius of the 10 classes
radius = [[]]*10
for i in range(0, 10):
    squared = (train_in[train_out[0] == i] - centroids.iloc[i, :])**2
    radius[i] = np.sum(squared, axis = 1).max()**(0.5)
    

# Sample size in each groups
from collections import Counter
n = Counter(train_out[0])

# Distance between 10 centers of classes
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
dist_cen = pdist(centroids, 'euclidean')
dist_mat = squareform(dist_cen)

##########
# Task 2 #
##########

out_label = []
for i in range(0, 1707):
    squared = (train_in.loc[i, :] - centroids)**2
    dist = np.sum(squared, axis = 1)**(0.5)
    out_label.append(np.argmin(dist))
    

out_label_test = []
for i in range(0, 1000):
    squared = (test_in.loc[i, :] - centroids)**2
    dist = np.sum(squared, axis = 1)**(0.5)
    out_label_test.append(np.argmin(dist))
    

import sklearn.metrics.pairwise




