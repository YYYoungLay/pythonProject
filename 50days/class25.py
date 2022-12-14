#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/12/14 16:51
# @Author: Ylei
# @File  : class25.py
# @Topic : 正则表达式的应用

import re

username = 'Young'
qq = '213454356'
#match函数的第一个参数是正则表达式字符串或正则表达式对象
#match函数的第二个参数是要跟正则表达式做匹配的字符串对象
m1 = re.match(r'[0-9a-zA-Z_]{6,20}$', username)
if not m1:
    print('username invalid')
#fullmatch函数要求字符串和正则表达式完全匹配
#所以正则表达式没有写起始符和结束符
m2 = re.fullmatch(r'[1-9]\d{4,11}', qq)
if not m2:
    print('qq invalid')
if m1 and m2:
    print('message valid!')
"""在线测试工具
https://c.runoob.com/front-end/854/
"""