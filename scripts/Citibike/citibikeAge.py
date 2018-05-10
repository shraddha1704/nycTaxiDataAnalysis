#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 01:28:26 2018

@author: risabh
"""
from collections import defaultdict
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import ks_2samp
import math

f = open("trips_clean.csv", "r")
age=defaultdict(int)
f.readline()
temp=[]
for line in f.readlines():
    val = 2018-int(line.split(",")[4])
    if val<80:
        temp.append(val)
        age[val]+=1 # Obtaining frequency count for different age groups
f.close()

lists = sorted(age.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples
#Calculating mean and variance for the data
val =0
for a in range(len(x)):
    
    val+=x[a]*y[a]

mean = val/sum(y)

sd = np.std(temp)    

dist = np.random.poisson(30, len(temp))

#Finding the Ks statistic
stats, p= ks_2samp(temp, dist)
plt.plot(x, y)
plt.xlabel("Age of people")
plt.ylabel("Frequency of trips")
plt.title("Plot for Age v/s Frequency of Trips")
#plt.hist(dist,50)
plt.savefig("ks.png")


comp_stat = 1.36/math.sqrt(len(temp))