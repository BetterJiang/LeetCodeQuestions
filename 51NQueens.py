# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 08:32:26 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com


51 n-queens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.
为了达到此目的，任两个皇后都不能处于同一条横行、纵行或斜线上。
假设有两个皇后被放置在(i,j)和(k,l)的位置上，当且仅当|i-k|=|j-l| 时，两个皇后才在同一条对角线上。

（1）先从首位开始检查，如果不能放置，接着检查该行第二个位置，依次检查下去，
直到在该行找到一个可以放置一个皇后的地方，然后保存当前状态，转到下一行重复上述方法的检索。
（2）如果检查了该行所有的位置均不能放置一个皇后，说明上一行皇后放置的位置无法让
所有的皇后找到自己合适的位置，因此就要回溯到上一行，重新检查该皇后位置后面的位置。

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

In this problem, we can go row by row, and in each position, we need to check
if the column, the 45° diagonal and the 135° diagonal had a queen before.

Solution A: 二维数组解法
    Directly check the validity of each position.
    board represents by n list[n] 棋盘
"""


def isValid(n, board, cr, cc):
    # cr current row, cc current column
    # check if the column had a queen before. same column different row
    for i in range(cr):
        if board[i][cc] == 'Q':
            return False
    # check if the 45° diagonal had a queen before. right diagonal
    # [cr-1, cr-2, cr-3, ..., 2, 1, 0] 0 is included.
    for i, j in zip(range(cr-1, -1, -1), range(cc+1, n, 1)):
        if board[i][j] == 'Q':
            return False
    # check if the 135° diagonal had a queen before. left diagonal
    for i, j in zip(range(cr-1, -1, -1), range(cc-1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True


def solveNQueens(n, res, board, cr):
    if cr == n:
        # res.append(board) will bring error filling matrix
        res.append([''.join(board[i]) for i in range(n)])
        return
    for j in range(n):
        if isValid(n, board, cr, j):
            board[cr][j] = 'Q'
            solveNQueens(n, res, board, cr + 1)  # move to the next row
            board[cr][j] = '.'  # why set as '.', donot understand!!!!!


def solveNQ(n):
    res = []
    board = [['.'] * n for _ in range(n)]
    solveNQueens(n, res, board, 0)  # start from row 0
    return res


if __name__ == "__main__":
    n = 4
    res = solveNQ(n)
    vec = [[0] * n for _ in res]
    for i in range(len(res)):
        vec[i] = [c.index('Q') for c in res[i]]  # 查看指定值在列表中的位置.index
    vec


"""
len(res)
a = res[0]
a
res

"""


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def isValid(n, board, cr, cc):
            # cr current row, cc current column
            # check if the column had a queen before. same column different row
            for i in range(cr):
                if board[i][cc] == 'Q':
                    return False
            # check if the 45° diagonal had a queen before. right diagonal
            # [cr-1, cr-2, cr-3, ..., 2, 1, 0] 0 is included.
            for i, j in zip(range(cr-1, -1, -1), range(cc+1, n, 1)):
                if board[i][j] == 'Q':
                    return False
            # check if the 135° diagonal had a queen before. left diagonal
            for i, j in zip(range(cr-1, -1, -1), range(cc-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            return True

        def solve(n, res, board, cr):
            if cr == n:
                # res.append(board) will bring error filling matrix
                # res.append([list(board[i]) for i in range(n)])
                res.append([''.join(board[i]) for i in range(n)])
                return
            for j in range(n):
                if isValid(n, board, cr, j):
                    board[cr][j] = 'Q'
                    solve(n, res, board, cr + 1)  # move to the next row
                    board[cr][j] = '.'

        res = []
        board = [['.'] * n for _ in range(n)]
        solve(n, res, board, 0)  # start from row 0
        return res

#sol2 = Solution()
sol = Solution()

res = sol.solveNQueens(4)
res
