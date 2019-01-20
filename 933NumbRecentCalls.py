# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 22:11:49 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com


933. Number of Recent Calls

inputs = ["RecentCounter","ping","ping","ping","ping"]
inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]

完全不知道在说什么
"""

#class RecentCounter:
#    def __init__(self):
#        self.p = collections.deque()
#
#    def ping(self, t):
#        self.p.append(t)
#        while self.p[0] < t - 3000:
#            self.p.popleft()
#        return len(self.p)


class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.queue and self.queue[0] < t-3000:
            self.queue.pop(0)
        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



