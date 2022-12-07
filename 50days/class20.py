#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/12/7 16:11
# @Author: Ylei
# @File  : class20.py
# @Topic : Python标准库初探

# TODO Base64编解码模
"""文本数据与二进制数据互转"""

# TODO collections
import random

"""collections-容量数据类型模块"""
# namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
# deque：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和删除元素是，deque会表现出更好的性能，渐近时间复杂度为$O(1)$。
# Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。Counter和dict的继承关系我认为是值得商榷的，按照CARP原则，Counter跟dict的关系应该设计为关联关系更为合理。
# OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。
# defaultdict：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法更加高效。

"""hashlib-哈希函数模块"""
import hashlib
#计算字符串‘young and rich’的MD5摘要
print(hashlib.md5('young and rich'.encode()).hexdigest())

# 计算文件 的MD5摘要
zipfile = 'E:/2-Programm/Github/KeymouseGo-master.zip'
with open(zipfile, 'rb') as file:
    data = file.read(512)
    while data:
        hashlib.md5().update(data)
        data = file.read(512)
print(hashlib.md5().hexdigest())

"""heapq-堆排序模块"""
import heapq
list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
#max
print(heapq.nlargest(4, list1))
#min
print(heapq.nsmallest(3, list1))
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list2, key=lambda x: x['price']))

"""litertools-迭代工具模块"""
import itertools
#‘ABCD’的全排列
# for value in itertools.permutations('ABCD'):
    # print(value)
#五选三组合
# for value in itertools.combinations('ABCD', 3):
#     print(value)
#ABCD和123的笛卡尔集
# for value in itertools.product('ABCD', '123'):
#     print(value)
#ABC的无限循环序列?
# it = itertools.cycle(('A', 'b', 'c'))
# print(next(it))
# print(next(it))

"""random-随机数和随机抽样模块"""
# getrandbits(k)：返回具有k个随机比特位的整数。??
print(random.getrandbits(8))
# randrange(start, stop[, step])：从range(start, stop, step) 返回一个随机选择的元素，但实际上并没有构建一个range对象。
print(random.randrange(2, 990, 5))
# randint(a, b)：返回随机整数N满足a <= N <= b，相当于randrange(a, b+1)。
print(random.randint(1, 6))
# choice(seq)：从非空序列seq返回一个随机元素。 如果seq为空，则引发IndexError。
print(random.choice([32, 4, 6, 78, -3, 0]))
# choices(population, weight=None, *, cum_weights=None, k=1)：从population中选择替换，返回大小为k的元素列表。 如果population为空，则引发IndexError。
print(random.choices([32, 4, 6, 78, -3, 0], k=5))
# shuffle(x[, random])：将序列x随机打乱位置。??
print(random.shuffle([32, 4, 6, 78, -3, 0]))
# sample(population, k)：返回从总体序列或集合中选择k个不重复元素构造的列表，用于无重复的随机抽样。
print(random.sample([32, 4, 6, 78, -3, 0, 0, 0, 0, 0], 4))
print(random.sample({1, 2, 3, 4, 5, 8, 8}, 4))
# random()：返回[0.0, 1.0)范围内的下一个随机浮点数。
print(random.random())
# expovariate(lambd)：指数分布。
print(random.expovariate(423))
# gammavariate(alpha, beta)：伽玛分布。
# gauss(mu, sigma) / normalvariate(mu, sigma)：正态分布。
# paretovariate(alpha)：帕累托分布。
# weibullvariate(alpha, beta)：威布尔分布。

"""os.path - 路径操作相关模块"""
import os.path
# dirname(path)：返回路径path的目录名称。
pathname = 'E:/5-临时创建/22年11月项目文档归档/2001-道路精准气象服务系统'
print(os.path.dirname(pathname))
# exists(path)：如果path指向一个已存在的路径或已打开的文件描述符，返回 True。
print(os.path.exists(pathname))
# getatime(path) / getmtime(path) / getctime(path)：返回path的最后访问时间/最后修改时间/创建时间。
print(os.path.getatime(pathname))
print(os.path.getmtime(pathname))
print(os.path.getctime(pathname))
# getsize(path)：返回path的大小，以字节为单位。如果该文件不存在或不可访问，则抛出OSError异常。
print(os.path.getsize(pathname))
# isfile(path)：如果path是普通文件，则返回 True。
print(os.path.isfile(pathname))
# isdir(path)：如果path是目录（文件夹），则返回True。
print(os.path.isdir(pathname))
# join(path, *paths)：合理地拼接一个或多个路径部分。返回值是path和paths所有值的连接，每个非空部分后面都紧跟一个目录分隔符 (os.sep)，除了最后一部分。这意味着如果最后一部分为空，则结果将以分隔符结尾。如果参数中某个部分是绝对路径，则绝对路径前的路径都将被丢弃，并从绝对路径部分开始连接。
print(os.path.join(pathname, '123.doc'))
# splitext(path)：将路径path拆分为一对，即(root, ext)，使得root + ext == path，其中ext为空或以英文句点开头，且最多包含一个句点
print(os.path.split(pathname))

"""uuid- UUID生成模块"""
import uuid
# uuid1()：由MAC地址、当前时间戳、随机数生成，可以保证全球范围内的唯一性。
print(uuid.uuid1().hex)
# uuid3(namespace, name)：通过计算命名空间和名字的MD5哈希摘要（“指纹”）值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字会生成相同的UUID。
# print(uuid.uuid3(23, 23))
# uuid4()：由伪随机数生成UUID，有一定的重复概率，该概率可以计算出来。
print(uuid.uuid4())
# uuid5()：算法与uuid3相同，只不过哈希函数用SHA-1取代了MD5。
# print(uuid.uuid5(23, 23))