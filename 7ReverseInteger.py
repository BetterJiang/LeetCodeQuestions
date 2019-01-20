# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:59:09 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

7. Reverse Integer

x = -321
reverse(x)

"""


def reverse(x):
    INT_MAX = 2**(31) - 1
    INT_MIN = -2**(31)
    rev = 0
    if x < 0:
        flag = True
        a = -x
    else:
        flag = False
        a = x
    while a != 0:
        pop = a % 10
        a //= 10
        if (rev > INT_MAX / 10 or (rev == INT_MAX / 10 and pop > 7)):
            return 0
        if (rev < INT_MIN / 10 or (rev == INT_MIN / 10 and pop < -8)):
            return 0
        rev = 10 * rev + pop
    if flag:
        return -rev
    else:
        return rev

