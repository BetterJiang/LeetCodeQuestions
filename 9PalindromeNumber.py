# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:52:52 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

9. Palindrome Number

Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left,
it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Coud you solve it without converting the integer to a string?

Reverse the number the if they are the same, x is palindrome

x = 121
x = -121
x = 123

isPalindrome(x)

"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    rev = 0
    a = x
    while a != 0:
        pop = a % 10
        a //= 10
        rev = 10 * rev + pop
    if rev == x:
        return True
    return False











