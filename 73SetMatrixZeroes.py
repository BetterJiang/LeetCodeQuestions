# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 15:02:22 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com


73. Set Matrix Zeroes
Follow up:
    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

"""


def setZeroes_v1(matrix):
    """
    Time Complexity:
        O(MN) where M and N are the number of rows and columns respectively.
    Space Complexity:
        O(M+N)
    """
    if not matrix:
        return []
    n, m = len(matrix), len(matrix[0])
    ZeroIdx = [(i, j) for i in range(n) for j in range(m) if matrix[i][j] == 0]
    for (i, j) in ZeroIdx:
        matrix[i][:] = [0]*m
        for k in range(n):
            matrix[k][j] = 0


def setZeroes_s1(matrix):
    """
    Time Complexity:
        O(MN) where M and N are the number of rows and columns respectively.
    Space Complexity:
        O(M+N)
    """
    if not matrix:
        return []
    n, m = len(matrix), len(matrix[0])
    rowSet, colSet = set(), set()
    # Essentially, we mark the rows and columns that are to be made zero
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rowSet.add(j)
                colSet.add(j)
    # Iterate over the array once again and using the rows and cols sets,
    # update the elements
    for i in range(n):
        for j in range(m):
            if i in rowSet or i in colSet:
                matrix[i][j] = 0


def setZeroes_v2(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    matrix = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
    Time Complexity: O((M*N)*(M+N))
    Space Complexity: O(1)
    """
    auxiliary = 'A'
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # We modify the elements in place.
                # Note, we only change the non zeros to auxiliary
                for c in range(m):
                    matrix[i][c] = auxiliary if matrix[i][c] != 0 else 0
                for r in range(n):
                    matrix[r][j] = auxiliary if matrix[r][j] != 0 else 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == auxiliary:
                matrix[i][j] = 0


def setZeroes_v3(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    matrix = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
    Time Complexity: O((M*N))
    Space Complexity: O(1)
    We can rather use the first cell of every row and column as a flag.
    This flag would determine whether a row or column has been set to zero.
    This means for every cell instead of going to (M+N) cells and setting it
    to zero we just set the flag in two cells.
    matrix = [[0,1,2,0], [3,0,5,2], [1,3,1,5]]
    """
    is_col = False
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        # Since first cell for both first row and first column is the same
        # i.e. matrix[0][0]
        # We can use an additional variable for either the first row/column.
        # Here we are using an additional variable for the first column
        # and using matrix[0][0] for the first row.
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, m):
            # If an element is zero, we set the first element of the
            # corresponding row and column to 0. begins with 2nd column, j=1
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # corresponding row
                matrix[0][j] = 0  # corresponding column
    # Iterate over the array again and using the first row and first column,
    # update the elements.
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    # See if the first row needs to be set to zero as well
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    # See if the first column needs to be set to zero as well
    if is_col:
        for i in range(n):
            matrix[i][0] = 0


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        matrix = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
        Time Complexity: O((M*N))
        Space Complexity: O(1)
        We can rather use the first cell of every row and column as a flag.
        This flag would determine whether a row or column has been set to zero.
        This means for every cell instead of going to (M+N) cells and setting it
        to zero we just set the flag in two cells.
        """
        is_col = False
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            # Since first cell for both first row and first column is the same
            # i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # Here we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, m):
                # If an element is zero, we set the first element of the
                # corresponding row and column to 0. begins with 2nd column, j=1
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # corresponding row
                    matrix[0][j] = 0  # corresponding column
        # Iterate over the array again and using the first row and first column,
        # update the elements.
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(n):
                matrix[i][0] = 0


if __name__ == "__main__":
    matrix = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
    sol = Solution()
    sol.setZeroes(matrix)
    matrix














