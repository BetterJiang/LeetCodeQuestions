# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 19:18:52 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""

import math
import os
import random
import re
import sys


# =============================================================================
# Since the question only asks the number of bribes, there's no need to really
# do a sorting, nor element swapping, nor "bubbling up" an element. All you need
# to do is to count the number of people who overtake a person.
# calc(q)
# =============================================================================

# Complete the minimumBribes function below.

def minimumBribes(q):
    # this is calculate all the inverse order of all the numbers
    inverseOrder = {}
    m = len(q)
    for i in range(m-1):
        v = q[i]
        k = 0
        for s in q[(i+1):m]:
            if v > s:
                k = k + 1
        inverseOrder[v] = k
    if max(inverseOrder.values()) > 2:
        print("Too chaotic")
    else:
        print(sum(inverseOrder.values()))


def minimum_bribes(q):
    inverseOrder = {}
    m = len(q)
    for i in range(m-1):
        v = q[i]
        k = 0
        for s in q[(i+1):m]:
            if v > s:
                k = k + 1
        inverseOrder[v] = k
        if inverseOrder[v] > 2:
            print("Too chaotic")
            return
    print(sum(inverseOrder.values()))


def calc(q):
    ans = 0
    m = len(q)
    i = m - 1
    while i >= 0:
        if (q[i] - (i + 1) > 2):
            print("Too chaotic")
            return
        for j in range(max(0, q[i]-2), i+1):
            if (q[j] > q[i]):
                ans += 1
        i -= 1
    return ans


q = [1, 5, 4, 2, 3]
q = [1, 3, 4, 6, 7, 5, 2]

q = [5, 1, 2, 3, 7, 8, 6, 4]
q = [1, 2, 5, 3, 7, 8, 6, 4]

q = [2, 1, 5, 3, 4]
q = [2, 5, 1, 3, 4]

minimumBribes(q)
minimum_bribes(q)
calc(q)




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)