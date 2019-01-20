# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:15:35 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

performing a simple linear search. The strategy is to see if the target is
smaller than then the last element in each list.
"""


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 3


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:  # if nothing is there
            return False
        i = 0
        while i < len(matrix) - 1 and matrix[i][-1] < target:
            i += 1
        if target in matrix[i]:
            return True
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 3

sol = Solution()
sol.searchMatrix(matrix, target)

matrix = [[]]


sol.searchMatrix([[]], target)

"""
测试特殊情形. matrix = [[]]

"""






