# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:46:09 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

num1 = '123456789123456789123456789123456789123456789'
以字符串（c++ string）的形式给定两个非负整数，num1和num2，返回两个数的乘积。
num1 = '123456789123456789123456789123456789123456789'
num2 = num1

rev_num1 = num1[::-1]
rev_num2 = num2[::-1]


num = '123'
k = '6'
num = '99'
k = '9'
kmultiply(num, k)



num1 = '123'
num2 = '16'

mult_list = multiply(num1, num2)


num1 = '738'
num2 = '1230'
add_strnum(num1, num2)


num1 = '123'
num2 = '116'
mult_list = multiply(num1, num2)
add_strnum(*mult_list)

multiply_strnum(num1, num2)

#reduce(add_strnum, mult_list)

99 * 999
multiply_strnum('99', '999')

90 * 909
multiply_strnum('90', '909')

123 * 116
multiply_strnum('123', '116')


"""


def kmultiply(num, k):
    m = len(num)
    res = ''
    carry = 0
    a = int(k)
    for i in range(m-1, -1, -1):
        g = int(num[i]) * a + carry
        carry, val = g // 10, g % 10
        res += str(val)
    if carry != 0:
        res += str(carry)
    km = res[::-1]
    return km


def add_2strnum(num1, num2):
    m1 = len(num1)
    m2 = len(num2)
    rev1 = num1[::-1]
    rev2 = num2[::-1]
    if m1 > m2:
        m1, m2 = m2, m1
        rev1, rev2 = rev2, rev1
    v1, v2 = '0', '0'
    res = ''
    carry = 0
    for i in range(m2):
        v2 = rev2[i]
        if i < m1:
            v1 = rev1[i]
        else:
            v1 = '0'
        g = int(v1) + int(v2) + carry
        carry, val = g // 10, g % 10
        res += str(val)
    s = res[::-1]
    return s


def add_strnum(*strnum_list):
    s = ''
    for num in strnum_list:
        s = add_2strnum(s, num)
    return s


def multiply(num1, num2):
    """
    """
    rev_num2 = num2[::-1]
    m2 = len(rev_num2)
    res = []
    for i in range(m2):
        k = rev_num2[i]
        km = kmultiply(num1, k)
        km += '0' * i
        res.append(km)
    return res


def multiply_strnum(num1, num2):
    mult_list = multiply(num1, num2)
    mult = add_strnum(*mult_list)
    return mult


if __name__ == '__main__':
    num1 = '123456789123456789123456789123456789123456789'
    num2 = num1
    mult = multiply_strnum(num1, num2)
    mult

