# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 19:46:49 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""


class Multiply(object):
    def kmultiply(self, num, k):
        m, m1 = len(num), len(k)
        if m == 1 and m1 != 1:
            num, k = k, num  # change the position
            m, m1, m1, m
        res = ''
        carry = 0
        a = int(k)
        for i in range(m-1, -1, -1):
            g = int(num[i]) * a + carry
            carry, val = g // 10, g % 10
            res += str(val)
        # need to judge if there left the numbers, to check 999 * 999
        if carry != 0:
            res += str(carry)
        km = res[::-1]
        return km

    def add_strnum(self, num1, num2):
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
        sadd = res[::-1]  # reverse the string
        return sadd

    def multiply(self, num1, num2):
        """
        num1, num2 are strings, and inside are nonnegative num[0~9]
        begins with not zero
        """
        rev_num2 = num2[::-1]
        m2 = len(rev_num2)
        res = ''  # by adding directly
        for i in range(m2):
            k = rev_num2[i]
            km = self.kmultiply(num1, k)
            km += '0' * i  # append with (i)zeroes, represent the ith position.
            res = self.add_strnum(res, km)
        return res

    def add_strnum_list(self, *strnum_list):
        s = ''
        for num in strnum_list:
            s = self.add_strnum(s, num)
        return s

    def multiply_strnum(self, num1, num2):
        """
        num1, num2 are strings, and inside are nonnegative num[0~9]
        begins with not zero
        return a list
        """
        rev_num2 = num2[::-1]
        m2 = len(rev_num2)
        res = []
        # of course not saving a list, but adding directly
        for i in range(m2):
            k = rev_num2[i]
            km = self.kmultiply(num1, k)
            km += '0' * i  # append with (i)zeroes, represent the ith position.
            res.append(km)
        return res

    def multiply2(self, num1, num2):
        mult_list = self.multiply_strnum(num1, num2)
        res = self.add_strnum_list(*mult_list)
        return res


if __name__ == '__main__':
    mult = Multiply()

    123 * 116
    num1 = '123'
    num2 = '116'
    mult.multiply(num1, num2)
    mult.multiply2(num1, num2)

    987 * 654
    num1 = '987'
    num2 = '654'
    mult.multiply(num1, num2)
    mult.multiply2(num1, num2)

    900 * 102030
    num1 = '900'
    num2 = '102030'
    mult.multiply(num1, num2)
    mult.multiply2(num1, num2)

    999 * 999
    num1 = '999'
    num2 = '999'
    mult.multiply(num1, num2)

    num1 = '123456789123456789123456789123456789123456789'
    num2 = num1
    mult.multiply(num1, num2)



















