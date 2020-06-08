#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:10:40 2020

@author: rjkg
"""

import numpy as np 
import pandas as pd

data= pd.read_csv("E:\Parkhi/find_s.csv")
print(data)

d = np.array(data)[:,:-1] 
print(d) 

target = np.array(data)[:,-1] 
print(target)
def find_s(c,t):
    for i,var in enumerate(t):
        if var =="Yes":
            specific_hypothesis = c[i].copy()
            break 
    for i,var in enumerate(c):
        if t[i]=="Yes":
            for r in range(len(specific_hypothesis)):
                if var[r] != specific_hypothesis[r]:
                    specific_hypothesis[r]= "?"
                else:
                    pass
    return specific_hypothesis 

print("The required hypothesis is :",find_s(d,target))
        
        