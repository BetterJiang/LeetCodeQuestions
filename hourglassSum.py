# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:43:06 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""

import math
import os
import random
import re
import sys

import numpy as np

arr = np.array(np.arange(36).reshape((6, 6)))


arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]


# Complete the hourglassSum function below.
def hourglassSum(arr):
    k = 0
    m, n = arr.shape
    vmax = -100
    for i in range(1, m-1):
        for j in range(1, n-1):
            k = k+1
            a = arr[(i-1):(i+2), (j-1):(j+2)].sum()
            if (a > vmax):
                vmax = a
    return vmax, k


def hourglassSum2(arr):
    k = 0
    vmax = -100
    m = len(arr[0])
    for i in range(1, m-1):
        h0 = arr[i]
        h1 = arr[i-1]
        h2 = arr[i+1]
        for j in range(1, m-1):
            k = k+1
            a = sum(h1[(j-1):(j+2)]) + sum(h2[(j-1):(j+2)]) + h0[j]
            if (a > vmax):
                vmax = a
    return vmax, k


# Enter your code here. Read input from STDIN. Print output to STDOUT
def hourglass(arr, s, t):
    sum = 0
    sum += arr[s][t]+arr[s][t+1]+arr[s][t+2]
    sum += arr[s+2][t]+arr[s+2][t+1]+arr[s+2][t+2]
    sum += arr[s+1][t+1]
    return sum


max = -70
for i in range(0, 4):
    for j in range(0,4):
        temp = hourglass(arr, i, j)
        if(max < temp):
            max = temp
print max
