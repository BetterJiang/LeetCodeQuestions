# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:36:23 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

Given an array of integers, return **indices** of the two numbers such that
they add up to a specific target. You may assume that each input would have
**exactly** one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
Not very clear:
    1. The given nums are in incremental order, or diminishing order?
    (no need for ordered/sorted nums.)
    2. Should I calculate all the combinations of the two sum?
    (no need to calculate all, find one is OK.)
Solution Idea:
    just to note down the pairs of (i, target - num)

"""


"""
brute force approach -- 蛮力计算法 -- computation complexity O(n^2), space O(1)
For each element, we try to find its complement by looping through the rest
of array which takes O(n) time. Therefore, the time complexity is O(n^2).
"""

nums = [9, 11, 23, 2, 7, 4]
target = 9

n = len(nums)
for i in range(0, n):
    for j in range(i + 1, n):
        if (nums[j] == target - nums[i]):
            print([i, j])


def TwoSumV1(nums, target):
    n = len(nums)
    for i in range(0, n):
        for j in range(i + 1, n):
            if (nums[i] + nums[j] == target):
                return([i, j])


TwoSumV1(nums, target)

"""
Two-pass Hash Table -- 双行程哈希表
calculate the remainder, 计算目标函数减掉当前值之后的余数。
"""

nums = [9, 11, 23, 2, 7, 4]
target = 9
my_dict = {}
n = len(nums)
for i in range(n):
    my_dict.update({nums[i]: i})
for i in range(n):
    r = target - nums[i]
    if r in my_dict:
        print(my_dict[r], i)
        break


nums = [9, 11, 23, 2, 7, 4]
target = 9
my_dict = {}
for idx, val in enumerate(nums):
    r = target - val
    if r in my_dict:
        print(my_dict[r], idx)
        break
    my_dict[val] = idx


def twoSum(nums, target):
    """
    my_dict save the (val: idx) pairs, 放到字典中
    只有val不重复时,作为key, (val: idx)唯一;
    当有重复的val时候，(val: idx) 后面的idx覆盖前面的
    """
    my_dict = {}  # a dictionary to map the value of nums and the index in nums
    for idx, val in enumerate(nums):
        r = target - val
        if r in my_dict:
            return [my_dict[r], idx]
        my_dict[val] = idx
    return [-1, -1]


class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_dict = {}
        for i in range(len(nums)):
            val = nums[i]
            r = target - nums[i]
            if r not in target_dict:
                target_dict[val] = i
            else:
                return [target_dict[r], i]
        return [-1, -1]


nums = [9, 11, 23, 2, 7, 4]
nums = [1, 2, 3, 4, 5, 6, 11, 23, 2, 7, 4]
target = 90
solut = Solution()
solut.twoSum(nums, target)

# only find one possible solution, not all the solutions.


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for idx, val in enumerate(nums):
            r = target - val
            if r not in my_dict:
                my_dict[val] = idx
            else:
                return[my_dict[r], idx]
        return[-1, -1]
