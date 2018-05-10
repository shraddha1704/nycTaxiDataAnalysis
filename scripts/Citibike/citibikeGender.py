#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:35:37 2018

@author: risabh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from scipy import stats

data = pd.read_csv('trips_clean.csv')
#print data.values
dist =  data[['gender','trip_duration']]

distVals = dist.values
mean = np.mean(dist[['trip_duration']])
stdDev = np.std(dist[['trip_duration']])
T = abs(dist[['trip_duration']] - mean) < .75 * stdDev
#T = abs(dist[['trip_duration']])  < 2000
#print T
data_wo_outlier = distVals[np.array(T).flatten()]

male=[]
female=[]
for i in data_wo_outlier:
    if(i[0]==1):
        male.append(i[1])
    elif(i[0]==2):
        female.append(i[1])
print(len(male))

mmean = np.mean(male)
fmean = np.mean(female)

theta_hat = mmean-fmean
t_obs=np.abs(theta_hat)

mstd = np.std(male)
fstd = np.std(female)
se_hat = np.sqrt(mstd**2/len(male) + fstd**2/len(female) )
W = t_obs/se_hat


from scipy.stats import norm
p=1-norm.cdf(W)

a=(theta_hat, theta_hat+1.95*se_hat, theta_hat-1.95*se_hat)