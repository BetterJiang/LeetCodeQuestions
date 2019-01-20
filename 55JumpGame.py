# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:54:05 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

55. Jump Game

Given an array of non-negative integers, you are initially positioned at the
first index of the array. Each element in the array represents your maximum
jump length at that position.

Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation:
    You will always arrive at index 3 no matter what. Its maximum
    jump length is 0, which makes it impossible to reach the last index.



Time complexity :
    O(2^n). There are 2^n (upper bound) ways of jumping from the first position
    to the last, where n is the length of array nums.
Space complexity :
    O(n). Recursion requires additional memory for the stack frames.

"""


def canJumpFromPosition_v1(position, nums):
    n = len(nums)
    if position == n - 1:
        return True
    furtherJump = min(position + nums[position], n - 1)  # furtherJump included
    for nextPosition in range(position + 1, furtherJump + 1):
        if canJumpFromPosition_v1(nextPosition, nums):
            return True
    return False


"""
One quick optimization we can do for the code above is
to check the nextPosition from right to left.
The theoretical worst case performance is the same, but in practice,
for silly examples, the code might run faster.
Intuitively, this means we always try to make the biggest jump such that
we reach the end as soon as possible
The change required is:
"""


def canJumpFromPosition_s1(position, nums):
    n = len(nums)
    if position == n - 1:
        return True
    furtherJump = min(position + nums[position], n - 1)  # furtherJump included
    for nextPosition in range(furtherJump, position, -1):
        if canJumpFromPosition_s1(nextPosition, nums):
            return True
    return False


def canJump_v1(nums):
    return canJumpFromPosition_v1(0, nums)


def canJump_s1(nums):
    return canJumpFromPosition_s1(0, nums)


"""
nums = [3,2,1,0,4]
canJump_v1(nums)
canJump_s1(nums)

nums = [2,3,1,1,4]
canJump_v1(nums)
canJump_s1(nums)

nums = [1,2,3,4]
canJump_v1(nums)
canJump_s1(nums)

"""

"""
Approach 2: Dynamic Programming Top-down
Top-down Dynamic Programming can be thought of as optimized backtracking.
It relies on the observation that once we determine that a certain index is
good / bad, this result will never change. This means that we can store the
result and not need to recompute it every time.
"""


def canJumpFromPosition(memo, position, nums):
    if memo[position] != 'UNKNOWN':
        return True if memo[position] == 'GOOD' else False
    n = len(nums)
    if position == n - 1:
        return True
    furtherJump = min(position + nums[position], n - 1)  # furtherJump included
    for nextPosition in range(position + 1, furtherJump + 1):
        if canJumpFromPosition(memo, nextPosition, nums):
            memo[position] = 'GOOD'
            return True
    memo[position] = 'BAD'
    return False


def canJump(nums):
    n = len(nums)
    memo = ['UNKNOWN'] * len(nums)
    memo[n - 1] = 'GOOD'
    return canJumpFromPosition(memo, 0, nums)




"""
nums = [1,2,3,4]
canJump_v1(nums)
canJump_s1(nums)
canJump(nums)

"""



class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """









