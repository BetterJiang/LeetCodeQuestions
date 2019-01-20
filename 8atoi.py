# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:49:17 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

8. String to Integer (atoi)

'0' in (''.join(str(i)) for i in range(10))

s = 'o-ij ---98mf'
atoi(s)
s = '   -345jjjjjj'
atoi(s)
s = '---345jjjjjj'
atoi(s)
s = '       '
atoi(s)

s = '   +345jjjjjj'
atoi(s)


"""


def atoi(s):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    n = len(s)
    k = 0
    while k <= n-1 and s[k] == ' ':
        k += 1
    if k >= n - 1:
        return 0
    sign = 1
    if s[k] == '-' or s[k] == '+':
        sign = 1 - 2 * (s[k] == '-')
        k += 1
    base = 0
    while k < n and (s[k] >= '0' and s[k] <= '9'):
        if (base > INT_MAX / 10 or (base == INT_MAX / 10 and int(s[k]) > 7)):
            if (sign == 1):
                return INT_MAX
            else:
                return INT_MIN
        base = 10 * base + (int(s[k]))
        k += 1
    return base * sign


def stract_numb(s):
    sign = 0
    nums = []
    flagS = True
    for c in s:
        if c == '-' and not flagS:
            sign += 1
        elif c in (''.join(str(i)) for i in range(10)):
            flagS = False
            if sign % 2 == 1:
                nums.append(-int(c))
            else:
                nums.append(int(c))
            sign = 0
    return nums


