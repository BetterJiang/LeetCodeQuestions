# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:35:00 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

Longest Substring Without Repeating Characters

"""


def all_unique(s, start, end):
    # use set.
    my_set = set()
    for i in range(start, end):
        if s[i] in my_set:
            return False
        my_set.add(s[i])
    return True


s = 'ilovepython'
all_unique(s, 0, len(s))

len('ilovepyth')


def lengthOfLongestSubstring(s):
    n = len(s)
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if all_unique(s, i, j):
                ans = max(ans, j - i)  # [i, j) so it is j-i, not j-i+1
            else:
                break
    return ans


s = 'ilovepythoooon'
lengthOfLongestSubstring(s)


"""
improvement:
    In the naive approaches, we repeatedly check a substring to see if it has
    duplicate character. But it is unnecessary. If a substring sij from index
    i to j−1 is already checked to have no duplicate characters. We only need
    to check if s[j] is already in the substring sij​.

To check if a character is already in the substring, we can scan the substring,
which leads to an O(n^2) algorithm. But we can do better.

By using HashSet as a sliding window, checking if a character in the current
can be done in O(1).

A sliding window is an abstract concept commonly used in array/string problems.
 (left-closed, right-open).
We use HashSet to store the characters in current window [i,j) (j=i initially).
Then we slide the index j to the right. If it is not in the HashSet,
we slide j further. Doing so until s[j] is already in the HashSet.
At this point, we found the maximum size of substrings without duplicate
characters start with index i. If we do this for all i, we get our answer.

"""


def longest_substring_set(s):
    # use set to save the unique characters.
    # to find the maximum size of substrings without duplicate characters start with index i.
    n = len(s)
    ans, i, j = 0, 0, 0
    myset = set()
    while (i < n) & (j < n):
        # try to extend the range [i, j]
        if s[j] not in myset:
            myset.add(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            myset.remove(s[i])
            i += 1
    return ans


s = 'ilovepythoooon'
s = 'abcabcbbb'
lengthOfLongestSubstring(s)
longest_substring_set(s)


"""
Approach 3: Sliding Window Optimized
The above solution requires at most 2n steps. In fact, it could be optimized
to require only n steps. Instead of using a set to tell if a character exists
or not, we could define a mapping of the characters to its index. Then we can
skip the characters immediately when we found a repeated character.

The reason is that if s[j] have a duplicate in the range [i,j) with index j′,
we don't need to increase i little by little. We can skip all the elements
in the range [i,j′] and let i to be j′+1 directly.
"""


def longest_substring_dict(s):
    # use dict to save the unique characters and the corresponding index
    n = len(s)
    ans, i, j = 0, 0, 0
    mydict = dict()
    while i < n and j < n:
        # try to extend the range [i, j]
        if s[j] not in mydict:
            mydict[s[j]] = j
            j += 1
            ans = max(ans, j - i)
        else:
            mydict[s[j]] = j
            i = j + 1
            j = i
    return ans


s = 'abcabcbbb'
longest_substring_dict(s)


def longest_substring_dict(s):
    n = len(s)
    ans, i, = 0, 0
    mydict = dict()
    for j in range(n):
        if s[j] in mydict:
            # the next i, jump to the next of mydict[s[j]] + 1, j'+1
            i = max(i, mydict[s[j]] + 1)
        ans = max(ans, j - i + 1)
        mydict[s[j]] = j
        print(i)
    return ans


s = 'abcabcbbb'
longest_substring_dict(s)



