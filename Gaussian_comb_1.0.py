#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 20:19:14 2017

@author: Eric Baetscher
"""

import os

print (os.getcwd())
import numpy as np

import matplotlib.pyplot as plt


#NUMBER OF MULTIPLES
number_reps = 18

#SPACING PARAMETER:
spacing_param = 5

#Build list of midpoints
range_of_midpoints = ((number_reps-1) * spacing_param)
spacing_param_list = []
for iter00 in range(number_reps):
    spacing_param_list.append((iter00 * spacing_param) - (range_of_midpoints / 2))     
print(spacing_param_list)


#Gaussian_Kernel
def gaussian_kernel(scale,
                    width,
                    offset,
                    window_start,
                    windew_end,
                    number_of_samples):
    depvar = []
    
    indvar = np.linspace(window_start,windew_end,number_of_samples)
    
    for element1 in indvar:
        temp2 = (scale/np.sqrt(2 * np.pi * (width**2)) *
                 (np.exp(-(((element1 - offset)**2) / (2*(width**2))))))
        depvar.append(temp2)

    return indvar,depvar  

#Standard norm
x1 = []
y1 = []
x1,y1 = gaussian_kernel(1,1,0,-40,40,500)


width01 = 0.8
scale01 = 6

x2 = x1
y2 = np.zeros(len(x1))

for iter01 in range(number_reps):
    x_tmp0, y_tmp0 = gaussian_kernel(scale01, width01, spacing_param_list[iter01] , -40 , 40 ,500)
    y2 = y2 + y_tmp0
   

plt.figure()
#plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()
