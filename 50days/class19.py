# -*- coding: utf-8 -*-
# @Time    : 2022/12/5 19:56
# @Author  : JiangLai
# @FileName: class19.py
# @Software: PyCharm
# @Topic   ：函数使用进阶

import operator
"""关键字参数"""
def can_from_triangle(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")
    return a + b > c and a + c > b and b + c > a

print(can_from_triangle(1, 2, 3))#调用函数传入参数不指定参数名 按位置对号入座
print(can_from_triangle(a=1, b=2, c=3))#调用函数通过“参数名=参数值”的形式顺序传入参数
print(can_from_triangle(c=5, a=2, b=6))#调用函数通过“参数名=参数值”的形式不按顺序传入参数

"""命名关键字参数取代位置参数
函数调用必须以参数名=参数值的方式传参，命名关键字参数，是在函数的参数列表中，写在*之后的参数
"""
def can_from_triangle_2(*, a, b, c):#*前面的参数都是位置参数，而*后面的参数就是命名关键字参数
    print(f"a = {a}, b = {b}, c = {c}")
    return a + b > c and a + c > b and b + c > a
# print(can_from_triangle2(1, 2, 3))#can_from_triangle2() takes 0 positional arguments but 3 were given
print(can_from_triangle(a=1, b=2, c=3))#传参时必须使用“参数名=参数值”的方式，位置不重要
print(can_from_triangle(c=5, a=2, b=6))

def calc(*args):#*args并不能处理带参数名的参数
    result = 0
    for arg in args:
        result += arg
    return result
print(calc(1, 2, 3))#可变参数*args来接收任意数量的参数
# print(calc(a=1, b=2, c=3))#calc() got an unexpected keyword argument 'a'

"""可变参数和关键字参数
当不知道调用者会传入的参数个数，也不知道调用者会不会指定参数名，则同时启用以上
关键字参数会将传入的带参数名的参数组装成一个字典，参数名就是字典中键值对的键，参数值是字典键值对中的值
"""
def calc_2(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for karg in kwargs.values():
        result += karg
    return result

print(calc_2())
print(calc_2(1, 2, 3))
print(calc_2(a=2, c=5, b=4))
print(calc_2(1, 2, a=4, b=6))
#不带参数名的参数（位置参数）必须出现在带参数名的参数（关键字参数）之前
# print(calc_2(1, 2, a=4, b=5, 4))#SyntaxError: positional argument follows keyword argument

"""高阶函数
函数本身可作为函数的参数或返回值
"""

def calc_3(*args, init_value, op, **kwargs):
    result = init_value
    for arg in  args:
        result = op(result, arg)
    for karg in kwargs.values():
        result = op (result, karg)
        return result

def add(a, b):
    return a + b
def mul(a, b):
    return a * b
#调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可
print(calc_3(1, 2, init_value=5, op=add, f=3 ))
# print(calc_3(1, 3, 4))#calc_3() missing 2 required keyword-only arguments: 'init_value' and 'op'
print(calc_3(1, 2, init_value=1, op=mul, x=3, y=4, z=5))
print(calc_3(1, 2, 3, init_value=0, op=operator.add, x=4, y=5)) #10
print(calc_3(1, 2, init_value=1, op=operator.mul, x=3, y=4, z=5))    # 120

#filter实现对序列中元素的过滤，map实现对序列中元素的映射
#去掉整数列表中的技术，并对所有的偶数求平方得到一个新列表
def is_even(num):
    return num % 2 == 0
def square(num):
    return num**2
numbers1 = [35, 12, 8, 99, 60,52]
numbers2 = list(map(square, filter(is_even, numbers1)))
print(numbers2)
numbers2 = [num**2 for num in numbers1 if num%2 == 0]
print(numbers2)

# TODO Lambda函数需要多练习
"""Lambda函数 
是没有名字的函数，匿名函数，只能有一行代码，代码中的表达式产生的原酸结果就是这个匿名函数的返回值
"""
"""定义Lambda函数的关键字是lambda，后面跟函数的参数，多个参数用逗号分隔开；冒号后面部分是函数的执行体，通常是一个表达式，表达式的运算结果就是Lambda函数的返回值"""
numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers1)))
print(numbers2)
"""
注意下面的代码中的calc_4函数，它同时使用了可变参数、关键字参数、命名关键字参数，其中命名关键字参数要放在可变参数和关键字参数之间，传参时先传入可变参数，关键字参数和命名关键字参数的先后顺序并不重要。
"""
def calc_4(*args, init_value=0, op=lambda x, y: x + y, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result

# 调用calc函数，使用init_value和op的默认值
print(calc_4(1, 2, 3, x=4, y=5))    # 15
# 调用calc函数，通过lambda函数给op参数赋值
print(calc_4(1, 2, 3, x=4, y=5, init_value=1, op=lambda x, y: x * y))    # 120

import operator, functools

# 一行代码定义求阶乘的函数
fac = lambda num: functools.reduce(operator.mul, range(1, num + 1), 1)
# 一行代码定义判断素数的函数
is_prime = lambda x: x > 1 and all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(10))        # 3628800
print(is_prime(9))    # False

"""
可变参数
*参数：最常见的变量名是args，看到该变量名，一眼就知道变量args指向一个tuple对象
**参数：最常见的变量名是kwargs，看到该变量名，一眼就知道变量kwargs指向一个dict对象
关键字参数
函数调用时，指定参数名称，称为关键字参数（别和默认参数混淆，这里是函数调用）
函数调用时，关键字参数必须在普通参数的后面
默认参数
只执行一次 尽量使用不可变对象
命名关键字参数
必须使用关键字方式传递参数
def only_kw(a,*,b,c)
    print(a)
    print(b)
    print(c)
only_kw(100,b=1000,c=99) #b和c必须使用参数名传递参数
"""