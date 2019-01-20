# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 08:35:42 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

ReversedAdd
题目：
反转数字求和。假设输入的数据格式是两个lists，lists1 = [1, 2, 3], lists2 = [4, 5, 6]
反转后求和：321+654=975，输出[9, 7, 5]。
lists1 = [8], lists2 = [2, 1], lists = [2, 0]


题目变形2：
假设输入的数据格式是字符串"123，456"，反转后求和：321+654=975，输出975。
分析：
输入的是字符串，主要涉及到字符串到数字的转换，反转可用数字求余或字符串的反转。

"""


def reverse_list(lists):
    n = len(lists)
    lists2 = []
    for i in range(n-1, -1, -1):
        lists2.append(lists[i])
    return lists2



def reverse_pos_num(x):
    # x is a positive number
    a = x // 10
    if a == 0:
        return x
    y = 0
    a = x
    while a != 0:
        a, b = a // 10, a % 10
        y = y * 10 + b
    return y


def reversed_add(lists1, lists2):
    m = len(lists1)
    n = len(lists2)
    lists3 = []
    carry = 0
    for i in range(max(m, n)):
        if i > m-1:
            v1 = 0
        else:
            v1 = lists1[i]
        if i > n-1:
            v2 = 0
        else:
            v2 = lists2[i]
        s = v1 + v2 + carry
        carry, val = s // 10, s % 10
        lists3.append(val)
    lists = reverse_list(lists3)
    if lists[0] == 0:
        return (lists[1:])
    return lists


lists1 = [1, 2, 3]
lists2 = [4, 5, 6]

reversed_add(lists1, lists2)

lists1 = [8]
lists2 = [2, 1]




