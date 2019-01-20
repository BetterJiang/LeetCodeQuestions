# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:09:43 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com


send to yuqun.yu@huawei.com

x**3 + 20x**2 + 3x -10 = 0
二分法求根


"""


def f(x):
    return x ** 3 + 20 * x ** 2 + 3 * x - 10


def sol_binary(a, b, tol=1e-4):
    x = (a + b) / 2
    if abs(f(x)) < tol:
        return x
    if f(a) > 0 and f(b) < 0:
        a, b = b, a
    if f(x) > 0:
        return sol_binary(a, x, tol)
    if f(x) < 0:
        return sol_binary(x, b, tol)


def solution_path():
    """
    f(1)
    f(0.5)
    f(-1)
    f(-20)
    """
    a, b = 0.5, 1
    while f(b) < 0:
        b *= 2
    x1 = round(sol_binary(a, b, tol=1e-4), 5)
    # f(x1) < 1e-4
    a, b = -1, 0.5
    x2 = round(sol_binary(a, b, tol=1e-4), 5)
    # f(x2) < 1e-4
    a = -1
    while f(a) > 0:
        a *= 1.5
    b = -1
    x3 = sol_binary(a, b, tol=1e-4)
    # f(x3) < 1e-4
    return (x1, x2, x3)


if __name__ == '__main__':
    x1, x2, x3 = solution_path()
    x1, x2, x3
    f(x1) < 1e-4
    f(x2) < 1e-4
    f(x3) < 1e-4









