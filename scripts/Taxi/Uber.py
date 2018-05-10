#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:01:16 2018

@author: risabh
"""

from collections import defaultdict
from matplotlib import pyplot as plt
from datetime import datetime
import numpy as np
import math



f = open("taxi_clean.csv", "r")
print(f.readline().split(","))

uber_before_start = datetime.strptime("10/31/2013", "%m/%d/%Y")
uber_before_end = datetime.strptime("05/01/2014", "%m/%d/%Y")
uber_after_start = datetime.strptime("05/31/2014", "%m/%d/%Y")
uber_after_end = datetime.strptime("12/01/2014", "%m/%d/%Y")
m_gid = set([4,12,13,24,41,42,43,45,48,50,68,74,75,79,87,88,90,100,103,104,105,107,113,114,116,120,125,127,128,137,140,141,142,143,144,148,151,152,153,158,161,162,163,164,166,170,186,194,202,209,211,224,229,230,231,232,233,234,236,237,238,239,243,244,246,249,261,262,263])

before_count= defaultdict(int)
after_count= defaultdict(int)
before = defaultdict(float)
after = defaultdict(float)
before_low =defaultdict(int)
before_mid =defaultdict(int)
before_high =defaultdict(int)
after_low =defaultdict(int)
after_mid =defaultdict(int)
after_high =defaultdict(int)

temp=[]
for line in f.readlines():
    sp_arr= line.split(",")
    date = datetime.strptime(sp_arr[0].split()[0], "%m/%d/%Y")
    
    if date> uber_before_start and date< uber_before_end:
        if(int(sp_arr[10])in m_gid):
            """val = float(sp_arr[6])
            if(val<3):
                before_low[date]+=1
            elif(val<6):
                before_mid[date]+=1
            else:
                before_high[date]+=1
            """
                
            before[date]+=float(sp_arr[8])
            before_count[date]+=1
    elif date> uber_after_start and date< uber_after_end:
        if(int(sp_arr[10])in m_gid):
            """val = float(sp_arr(6))
            if(val<3):
                after_low[date]+=1
            elif(val<6):
                after_mid[date]+=1
            else:
                after_high[date]+=1
            """
            after[date]+=float(sp_arr[8])
            after_count[date]+=1
f.close()

lists = sorted(before.items()) # sorted by key, return a list of tuples

x, y = zip(*lists)


lists1 = sorted(after.items()) # sorted by key, return a list of tuples

l1,l2 = zip(*lists1)

count = [i for i in range(181)]
y_l = list(y)
l2_l = list(l2)[:-2]


def movingAverage(aggregatedRes, k):

    size = len(aggregatedRes)
    if(size <= k):
        return aggregatedRes

    res = list()
    sum1 = 0
    for i in range(0, k):
        sum1 = sum1 + aggregatedRes[i];
    index = 0;
    res.append( sum1 / k);

    for i in range(k, size):
        sum1 = sum1 - aggregatedRes[index];
        sum1 = sum1 + aggregatedRes[i];
        res.append(sum1 / k);
        index = index + 1;
    return res;


y_m = movingAverage(y_l, 10)
l2_m = movingAverage(l2_l, 10)
count1 = count[9:]
plt.scatter(count1,y_m,label='Before Uber ')

plt.scatter(count1,l2_m,label='After Uber')
plt.xlabel("Days")
plt.ylabel("Revenue ")
plt.title("Impact on Green taxi revenue by Uber")
plt.savefig("Uber Impact.png")
plt.legend()
plt.show()
diff=[]
for i in range(len(y_m)):
    diff.append(l2_m[i]-y_m[i])
    
avg = np.mean(diff)
std = np.std(diff)


t_val = math.sqrt(len(y_m))*avg/std

plt.savefig("Uber_final.png")

