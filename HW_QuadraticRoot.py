# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:34:43 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""


class QuadraticRoot(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def f(self, x):
        return self.a * x ** 3 + self.b * x ** 2 + self.c * x + self.d

    def g(self, x):
        return 3 * self.a * x ** 2 + 2*self.b * x + self.c

    def newton_recursive(self, init_x=0, tol=1e-4):
        x0 = init_x
        f0 = self.f(x0)
        g0 = self.g(x0)
        x1 = x0 - f0 / g0
        if abs(self.f(x0)) < tol:
            return x0
        return self.newton_recursive(x1, tol)

    def newton(self, init_x=0, tol=1e-4):
        x0 = init_x
        while abs(self.f(x0)) > tol:
            f0 = self.f(x0)
            g0 = self.g(x0)
            x0 -= f0 / g0
        return x0


if __name__ == '__main__':
    """
    cr.f(1)
    cr.f(0.5)
    cr.f(-0.5)
    cr.f(-1)
    cr.f(-2)
    cr.f(-20)
    """
    a, b, c, d = 1, 20, 3, -10
    cr = CubicRoot(a, b, c, d)
    t1, t2, t3 = 1.5, -1.5, -20
    x1, x2, x3 = cr.newton(t1), cr.newton(t2), cr.newton(t3)

    x1, x2, x3
    cr.f(x1) < 1e-4
    cr.f(x2) < 1e-4
    cr.f(x3) < 1e-4

    z1, z2 = cr.newton_recursive(t1), cr.newton_recursive(t2)
    z3 = cr.newton_recursive(t3)
    z1, z2, z3
    cr.f(z1) < 1e-4
    cr.f(z2) < 1e-4
    cr.f(z3) < 1e-4




