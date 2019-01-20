# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 22:44:07 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

"""

import os  # 导入os模块，模块的概念后面讲到
[d for d in os.listdir('.')]  # os.listdir可以列出文件和目录

s = "Hello World"

L1 = ['Hello', 'World', 18, 'Apple', None]

[s.lower() for s in L1]  # return error

[s.lower() for s in L1 if isinstance(s, str)]


list(range(4, -1, -1))

s = "Hello World"
lst = s.split()




