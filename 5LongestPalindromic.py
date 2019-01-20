# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:09:59 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

5. Longest Palindromic Substring 最长回文子串 ; 最长回文串 ; 最长连续回文串
A palindrome is a string which reads the same in both directions.
For example, s = "aba" is a palindrome, s = "abc" is not.

"""


"""
Approach 1: Longest Common Substring

Common mistake

Some people will be tempted to come up with a quick solution, which is
unfortunately flawed (however can be corrected easily):

Reverse S and become S'. Find the longest common substring between S and S',
which must also be the longest palindromic substring.

sometimes it is wrong

For example, S = "caba", S'= "abac".
The longest common substring between S and S' is "aba", which is the answer.

Let's try another example: S = "abacdfgdcaba", S' = "abacdgfdcaba".
The longest common substring between S and S' is "abacd".
Clearly, this is not a valid palindrome.


To find the reversed string:
    'hello world'[::-1]  # the reverse
    s0 = "abacdfgdcaba"
    s2 = s0[::-1]

We could see that the longest common substring method fails when there exists
a reversed copy of a non-palindromic substring in some other part of S.
To rectify this, each time we find a longest common substring candidate, we
check if the substring’s indices are the same as the reversed substring's
original indices. If it is, then we attempt to update the longest palindrome
found so far; if not, we skip this and find the next candidate.

This gives us an O(n^2) Dynamic Programming solution which uses O(n^2) space
(could be improved to use O(n) space).
Please read more about Longest Common Substring

Approach 2: Brute Force

Approach 3: Dynamic Programming
动态规划
动态规划的两个特点：第一大问题拆解为小问题，第二重复利用之前的计算结果。
先把所有长度最短为1的子字符串计算出来，根据起始位置从左向右，这些必定是回文。
然后计算所有长度为2的子字符串，再根据起始位置从左向右。
到长度为3的时候，就可以利用上次的计算结果：
如果中心对称的短字符串不是回文，那长字符串也不是，
如果短字符串是回文，那就要看长字符串两头是否一样。
这样，一直到长度最大的子字符串，我们就把整个字符串集穷举完了。

我们维护一个二维数组dp，其中dp[i][j]表示字符串区间[i, j]是否为回文串，
如果i = j，只有一个字符，肯定是回文串，
如果i = j + 1，说明是相邻字符，此时需要判断s[i]是否等于s[j]，
如果i和j不相邻，即i-j >= 2时，除了判断s[i]和s[j]相等之外，
dp[j+1][i-1]若为真，就是回文串，通过以上分析，可以写出递推式


"""

"""
s = "abacdfgdcaba"
s = 'ababad'
longest_palindrome_DP(s)
longest_palindrome_DynProg(s)


s = 'abc'
s = 'aaa'
longest_palindrome_DP(s)  # 对于相同的字符，会少一个
longest_palindrome_DynProg(s)

s[3]


"""


def longest_palindrome_DP(s):
    n = len(s)
    if n == 1:
        return s
    elif n > 1000:
        return ValueError
    dp = [[0]*n for _ in range(n)]
    start, end, maxL = 0, 0, 0
    # j controls the length of the substring, 所有长度为 (j+1) 的子字符串
    # dp[i][j] includes j. (i,j) 的起始点有点乱
    for j in range(n):
        for i in range(j):
            dp[i][j] = (s[i] == s[j]) & ((j - i < 2) | dp[i + 1][j - 1])
            if dp[i][j] and maxL < j - i + 1:
                maxL = j - i + 1
                start = i
                end = j
            dp[i][i] = 1
    return s[start:end + 1]


def longest_palindrome_DynProg(s):
    n = len(s)
    if n == 1:
        return s
    elif n > 1000:
        return ValueError
    dp = [[0]*n for _ in range(n)]
    start, end, maxL = 0, 0, 0
    # j controls the length of the substring, 所有长度为 (j+1) 的子字符串
    # dp[i][j] includes j.
    for j in range(n):
        for i in range(j+1):  # included j
            # 简单是简单，但是太抽象，但是如果j=0, j-1<0, 报错.
            # dp[i][j] = (s[i] == s[j]) & ((j - i < 2) | dp[i + 1][j - 1])
            if i == j:
                dp[i][j] = 1
            elif (j - i == 1) and s[i] == s[j]:
                dp[i][j] = 1
            elif (j - i >= 2) and s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = 1
            if dp[i][j] and maxL < j - i + 1:
                maxL = j - i + 1
                start = i
                end = j
    return s[start: end + 1]
















