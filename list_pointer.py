# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:03:29 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

ListNode 类型非常像 Iterator 对象。（迭代器）
Python 的 Iterator 对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出 StopIteration 错误。
可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，所以 Iterator 的计算是惰性的，
只有在需要返回下一个数据时它才会计算。

"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


a1 = [2, 3, 4, 5, 6]
n1 = len(a1)

l1 = ListNode(a1[0])
head = l1  # it is a must, to say that the head is the current l1
for i in range(1, n1):
    print(i)
    l1.next = ListNode(a1[i])
    l1 = l1.next

p = head

while p:
    print(p.val)
    p = p.next


def List2Pointer(a1):
    n = len(a1)
    l1 = ListNode(a1[0])
    head = l1  # it is a must, to say that the head is the current l1
    for i in range(1, n):
        l1.next = ListNode(a1[i])
        l1 = l1.next
    return head


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    curr = ListNode(0)
    dummyhead = curr
    carry = 0
    while l1 or l2 or carry:
        p = q = 0
        if l1:
            p = l1.val
            l1 = l1.next
        if l2:
            q = l2.val
            l2 = l2.next
        carry, val = divmod(p + q + carry, 10)
        curr.next = ListNode(val)
        curr = curr.next
    return dummyhead.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = ListNode(0)
        dummyhead = curr
        carry = 0
        while l1 or l2 or carry:
            p = q = 0
            if l1:
                p = l1.val
                l1 = l1.next
            if l2:
                q = l2.val
                l2 = l2.next
            carry, val = divmod(p + q + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
        return dummyhead.next



a1 = [2, 3, 4]
a2 = [4, 5, 6]

l1 = List2Pointer(a1)
l2 = List2Pointer(a2)

addTwoNumbers(l1, l2)




s = Solution()
a = s.addTwoNumbers(l1, l2)

while a:
    print(a.val)
    a = a.next



