# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:14:57 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

# Python program to find smallest and second smallest elements in an array.
The same approach can be used to find the largest and second largest elements
Time Complexity: O(n)

"""

# Python program to find smallest and second smallest elements
import sys


def print2Smallest_v1(arr):
    arr_size = len(arr)
    if arr_size < 2:
        print("Invalid Input")
        return
    first = second = sys.maxsize
    for i in range(0, arr_size):
        if arr[i] < first:
            # here we cannot change the order, update second first
            second = first
            first = arr[i]
        elif (arr[i] < second and arr[i] != first):
            second = arr[i]
    return(first, second)


def print2Smallest(arr):
    # There should be atleast two elements
    arr_size = len(arr)
    if arr_size < 2:
        print("Invalid Input")
        return
    first = second = sys.maxsize
    for i in range(0, arr_size):
        # If current element is smaller than first then
        # update both first and second
        if arr[i] < first:
            second = first
            first = arr[i]
        # If arr[i] is in between first and second then
        # update second
        elif (arr[i] < second and arr[i] != first):
            second = arr[i]
    if (second == sys.maxsize):
        print("No second smallest element")
    else:
        print('The smallest element is', first, 'and '
              'second smallest element is', second)


# Driver function to test above function
arr = [12, 13, 1, 10, 34, 1]
print2Smallest(arr)

print2Smallest_v1(arr)

# This code is contributed by Devesh Agrawal

