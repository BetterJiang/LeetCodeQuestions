# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:56:05 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""


class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


e1 = daynames('Mon')
e2 = daynames('Wed')
e3 = daynames('Tue')
e4 = daynames('Thu')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

e1.dataval
k = e1.nextval
k.dataval


thisvalue = e1
while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

h = list1.headval
h.dataval
h.nextval


list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


slist = SLinkedList()
slist.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")


# Link first Node to second node
slist.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
e3.nextval = e4


slist.listprint()


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        # Print the linked list
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        # Update the new nodes next val to existing node
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while laste.nextval:
            laste = laste.nextval
        laste.nextval = NewNode



slist = SLinkedList()
slist.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")

slist.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4


slist.AtBegining("Sun")

slist.listprint()

slist.AtEnd("Fri")


lists = [4, 0, 5, 8, 9, 3]
n = len(lists)
slist = SLinkedList()
slist.headval = Node(lists[0])

slist.listprint()
for i in range(1, n):
    slist.AtEnd(lists[i])


slist.listprint()




########################################


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        # Print the linked list
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        # Update the new nodes next val to existing node
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while laste.nextval:
            laste = laste.nextval
        laste.nextval = NewNode


def list2listNode(lists):
    n = len(lists)
    slist = SLinkedList()
    slist.headval = Node(lists[0])
    if n <= 1:
        return slist
    for i in range(1, n):
        slist.AtEnd(lists[i])
    return slist.headval



slist.listprint()



l1 = list2listNode([2, 4, 3])
l2 = list2listNode([5, 6, 4])

l1.dataval
l1.nextval


l1.listprint()








