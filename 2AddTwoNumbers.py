# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:11:50 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com


You are given two non-empty linked lists 链表 representing two non-negative integers.
The digits are stored in **reverse order** and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any **leading zero**,
except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
Visualization of the addition of two numbers: 342+465=807342 + 465 = 807
Each node contains a single digit and the digits are stored in reverse order.
"""


"""
链表, linked list, Definition for singly-linked list.
ListNode 是一种新的数据形式，像iterator 一样存在，但是会有两个parameter，
.val 直接得到数值; .next 得到下一个数值，如果是None 的话，表示这个list 已经遍历完了。

链表的基本元素有：
    节点：每个节点有两个部分，左边部分称为值域，用来存放用户数据；
    右边部分称为指针域，用来存放指向下一个元素的指针。
    head: head节点永远指向第一个节点
    tail: tail永远指向最后一个节点
    None: 链表中最后一个节点的指针域为None值

"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0  # 表示进位 carry bit
        dummyhead = curr = ListNode(0)
        # Initialize current node to dummy head of the returning list.
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            s = v1 + v2 + carry
            carry, val = s // 10, s % 10  # 整数部分，余数部分
            # carry, val = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next  # 整体指向 curr.next 作为当前链表。
        return dummyhead.next  # 最开始的初始化多加了一个None, 所以返回.next


def list2ListNode(lists):
    dummyhead = curr = ListNode(0)
    for val in lists:
        curr.next = ListNode(val)
        curr = curr.next  # 整体指向 curr.next 作为当前链表。
    return dummyhead.next  # 最开始的初始化多加了一个None, 所以返回.next


def printListNode(ListNode):
    printval = ListNode
    while printval is not None:
        print(printval.val)
        printval = printval.next
    return


l1 = list2ListNode([2, 4, 3, 8, 7])
printListNode(l1)


# check the sum
l1 = list2ListNode([2, 4, 3])
l2 = list2ListNode([5, 6, 4])
printListNode(l1)
printListNode(l2)
sol = Solution()
a = sol.addTwoNumbers(l1, l2)
printListNode(a)



l1 = list2ListNode([6, 9, 1])
l2 = list2ListNode([8, 9])
printListNode(l1)
printListNode(l2)
sol = Solution()
a = sol.addTwoNumbers(l1, l2)
printListNode(a)



