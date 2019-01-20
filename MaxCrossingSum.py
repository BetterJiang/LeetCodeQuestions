# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:18:50 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:54:29 2018
@author: HaiyanJiang
@email: jianghaiyan.cn@gmail.com

"""

# A Divide and Conquer based program for maximum subarray sum problem
# Find the maximum possible sum in arr[] such that arr[m] is part of it


def maxCrossingSum(arr, s, m, h):
    # Include elements on left of mid [s, h].
    sm = 0
    left_sum = -10000
    for i in range(m, s-1, -1):
        sm = sm + arr[i]
        if (sm > left_sum):
            left_sum = sm
    # Include elements on right of mid
    sm = 0
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]
        if (sm > right_sum):
            right_sum = sm
    # Return sum of elements on left and right of mid
    return left_sum + right_sum


def maxSubArraySum(arr, s, h):
    # Returns sum of maxium sum subarray in aa[l..h]
    # Base Case: Only one element
    if s == h:
        return arr[s]
    # Find middle point
    m = (s + h) // 2
    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half (both begins and ends in the left)
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the subarray crosses the midpoint
    return max(maxSubArraySum(arr, s, m),
               maxSubArraySum(arr, m+1, h),
               maxCrossingSum(arr, s, m, h))


# Driver Code
arr = [2, 3, -4, 5, 7]
n = len(arr)

max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)

# This code is contributed by Nikita Tiwari.
