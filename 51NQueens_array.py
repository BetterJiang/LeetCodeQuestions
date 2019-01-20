# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:32:33 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

这儿采用一维数组解决八皇后问题，即行数作为index，而列数代表array[index]。
conflict, 冲突检查，在定义state时，采用state来标志每个皇后的位置，其中索引用来
表示横坐标，其对应的值表示纵坐标。例如：state[0]=3，表示该皇后位于第1行的第4列上
"""


def conflict(state, pos):
    ns = len(state)
    for i in range(ns):
        # 如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，
        # 则说明有冲突，需要重新摆放
        if abs(state[i] - pos) in (0, ns-i):
            return True
    return False


# 采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            # 产生当前皇后的位置信息
            if len(state) == num - 1:
                yield (pos, )
            # 否则，把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
            else:
                for cur in queens(num, state+(pos,)):
                    yield (pos, ) + cur


def prettyprint(board):
    # 为了直观表现棋盘，用 X 表示每个皇后的位置
    def line(pos, length=len(board)):
        return '. ' * (pos) + 'X ' + '. '*(length-pos-1)
    for pos in board:
        print(line(pos))


if __name__ == "__main__":
    res = list(queens(8))
    prettyprint(res[1])
