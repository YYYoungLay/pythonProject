#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/12/8 16:50
# @Author: Ylei
# @File  : class23.py
# @Topic : 文件读写和异常处理

# TODO 文件操作

# TODO 异常处理机制
"""异常处理机制"""
file = None
try:
    file = open('main.py', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件！')
except LookupError:
    print('指定了未知的编码！')
except UnicodeEncodeError:
    print('读取文件时解码错误！')
finally:
    if file:
        file.close()
