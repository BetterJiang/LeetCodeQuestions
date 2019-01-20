# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:25:58 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com


4. Median of Two Sorted Arrays

step1: 将数据分成等长的两段，左段数值 <= 右端数值
    need to understand "What is the use of median".
    In statistics, the median is used for:
        Dividing a set into two equal length subsets,
        that one subset is always greater than the other.

if understand the use of median for dividing, we are very close to the answer.

step2: turn the problem into a binary search problem.


Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5


A = [1, 2]
B = [3, 4]
A = [1, 3]
B = [2]
median(A, B)

"""


def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        return ValueError
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and A[i] < B[j-1]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0:
                max_of_left = B[j-1]
            elif j == 0:
                max_of_left = A[i-1]
            else:
                max_of_left = max(A[i-1], B[j-1])
            if (m + n) % 2 == 1:
                # odd, when m+n is odd
                return max_of_left
            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])
            result = (max_of_left + min_of_right) / 2.0  # when m+n is even
            return result


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            return ValueError
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums1[i] < nums2[j-1]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 1:
                    # odd, when m+n is odd
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                result = (max_of_left + min_of_right) / 2.0  # when m+n is even
                return result

