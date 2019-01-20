# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:19:42 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

60. Permutation Sequence
If we have n numbers then the total combinations would be factorial(n)
which means same starting number should have (n - 1)! sequences.

If we do k mod (n - 1)!,
then we can get the corresponding starting number and append to the result.
Note that we need to maintain another array to mark visited numbers
(I take remove to make sure we will not revisit the number again,
each remove takes O(n) time )
The total time complexity would be O(n^2).

"""




class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(map(str, range(1, 10)))
        k -= 1
        factor = 1
        for i in range(1, n):
            factor *= i  # (n-1)!
        res = []
        for i in reversed(range(n)):
            res.append(nums[k // factor])
            nums.remove(nums[k // factor])
            if i != 0:
                k %= factor
                factor //= i
        return "".join(res)


sol = Solution()
sol.getPermutation(4, 2)


