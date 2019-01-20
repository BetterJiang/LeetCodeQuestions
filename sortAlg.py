# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:47:10 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""


"""
Title: 插入排序中的直接插入排序，依赖于初始序列
Description:
    在有序序列中不断插入新的记录以达到扩大有序区域到整个数组的目的
    时间复杂度：最好情形O(n)，平均情形O(n^2)，最差情形O(n^2)
    空间复杂度：O(1)
    稳定性：【稳定】
    内部排序(在排序过程中数据元素完全在内存)
"""


def insert_sort(lists):
    """插入排序--直接插入法。时间复杂度: O(n^2)"""
    n = len(lists)
    for i in range(1, n):
        cur = lists[i]
        j = i - 1
        while j >= 0:
            if cur < lists[j]:
                lists[j+1] = lists[j]
                lists[j] = cur
            j = j - 1
            print(i, "-->", lists)
    return lists


lists = [4, 9, 3, 8, 6, 5]
insert_sort(lists)


"""
希尔排序时效分析很难，关键码的比较次数与记录移动次数依赖于增量因子序列d的选取，
特定情况下可以准确估算出关键码的比较次数和记录的移动次数。
目前还没有人给出选取最好的增量因子序列的方法。
增量因子序列可以有各种取法，有取奇数的，也有取质数的.
但需要注意：增量因子中除1 外没有公因子，且最后一个增量因子必须为1。
希尔排序方法是一个【不稳定】的排序方法。
"""


def shell_sort(lists):
    """插入排序--希尔排序（Shell's Sort），缩小增量排序
    刚开始时，gap较大，每个子序列元素较少，排序速度较快；
    待到排序后期，gap变小，每个子序列元素较多，但大部分元素基本有序，所以排序速度仍较快。
    时间复杂度：O(n) ~ O(n^2)
    空间复杂度：O(1)
    稳 定 性：不稳定
    内部排序(在排序过程中数据元素完全在内存)
    """
    n = len(lists)
    gap = n
    while (gap > 1):
        gap = gap // 3 + 1
        for i in range(gap, n):
            j = i - gap
            while (j >= 0):
                cur = lists[j]
                if (cur > lists[j + gap]):
                    lists[j] = lists[j + gap]
                    lists[j + gap] = cur
                    print(gap, "-->", lists)
                j -= gap
    return lists


lists = [4, 9, 3, 8, 6, 5, 2]
shell_sort(lists)


"""
选择排序——直接选择排序，堆排序
直接选择排序的思想：
第一次从R[0]~R[n-1]中选取最小值，与R[0]交换，
第二次从R[1]~R[n-1]中选取最小值，与R[1]交换，……
第i次从R[i-1]~R[n-1]中选取最小值，与R[i-1]交换，……
第n-1次从R[n-2]~R[n-1]中选取最小值，与R[n-2]交换，
总共通过n-1次，得到一个按排序码从小到大排列的有序序列。
直接选择排序是一种【不稳定】的排序算法，
"""


def select_sort(lists):
    """
    Title:选择排序中的直接选择排序，依赖于初始序列
    Description: 每一趟 (例如第i趟，i = 0,1,...)
    在后面第n-i个待排序元素中选出最小元素作为有序序列的第i个元素
    时间复杂度：最好情形O(n^2)，平均情形O(n^2)，最差情形O(n^2)
    空间复杂度：O(1)
    稳 定 性：不稳定
    内部排序(在排序过程中数据元素完全在内存)
    """
    n = len(lists)
    for i in range(n):
        cur = lists[i]
        k, xmin = i, cur  # find the minumum and the corresponding min_index
        for j in range(i+1, n):
            if lists[j] < xmin:
                k, xmin = j, lists[j]
        lists[i] = xmin
        lists[k] = cur
        print(i, "-->", lists)
    return lists


lists = [4, 9, 3, 8, 6, 5, 2]
select_sort(lists)


def select_sort2(lists):
    n = len(lists)
    for i in range(n):
        min_index = i  # only keep records of the minimum index is OK
        for j in range(i+1, n):
            if lists[j] < lists[min_index]:
                min_index = j
        lists[min_index], lists[i] = lists[i], lists[min_index]
        print(i, "-->", lists)
    return lists


lists = [4, 9, 3, 8, 6, 5, 2]
select_sort2(lists)


"""
冒泡排序的思想：根据序列中两个元素的比较结果来对换这两个记录在序列中的位置，
将键值较大的记录向序列的尾部移动，键值较小的记录向序列的前部移动。
因此，每一趟都将较小的元素移到前面，较大的元素自然就逐渐沉到最后面了，
也就是说，最大的元素最后才能确定，这就是冒泡。冒泡排序是一种稳定的排序算法.
交换排序中的冒泡排序，一般情形下指的是优化后的冒泡排序，最多进行n-1次比较，依赖于初始序列
Description: 因为越大的元素会经由交换慢慢"浮"到数列的顶端(最后位置)，
最大的数最后才确定下来，所以称为冒泡排序
时间复杂度：最好情形O(n)，平均情形O(n^2)，最差情形O(n^2)
空间复杂度：O(1)
稳 定 性：稳定
内部排序(在排序过程中数据元素完全在内存)
"""


def swap2(lists, i, j):
    lists[i], lists[j] = lists[j], lists[i]
    return lists


def swap(lists, i, j):
    tmp = lists[i]
    lists[i] = lists[j]
    lists[j] = tmp
    return lists



lists = [4, 9, 3, 8, 6, 5, 2]
swap(lists, 0, 2)
swap(lists, 2, 0)

lists = [4, 9, 3, 8, 6, 5, 2]
swap2(lists, 2, 0)
lists = [4, 9, 3, 8, 6, 5, 2]
swap2(lists, 0, 2)


def bubble_sort(lists):
    n = len(lists)
    print("s -->", lists)
    for i in range(n):
        for j in range(i+1, n):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
                print(i, "-->", lists)
    return lists


lists = [4, 9, 3, 8, 6, 5, 2]
bubble_sort(lists)






