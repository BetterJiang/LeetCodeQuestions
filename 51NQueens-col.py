# -*- coding: utf-8 -*-
"""
roweated on Sun Nov  4 12:57:19 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""

global n


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil_v1(result, board, col):
    if col >= n:
        result.append(board)
        return True
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil_v1(result, board, col + 1):  # move to the next col
                return True
            board[i][col] = 0  # backtracking
    return False


def solveNQUtil(result, board, col):
    if col >= n:
        # result.append(board) will bring error filling matrix
        result.append([list(board[i]) for i in range(n)])
        return
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            solveNQUtil(result, board, col + 1)  # move to the next col
            board[i][col] = 0  # backtracking


def solveNQ(n):
    result = []
    board = [[0] * n for _ in range(n)]
    solveNQUtil(result, board, 0)  # start from col 0
    return result


if __name__ == "__main__":
    n = 8
    res = solveNQ(n)
    len(res)
    res[0]
    res




