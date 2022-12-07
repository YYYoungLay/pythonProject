#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/11/9 11:03
# @Author: Ylei
# @File  : helloword.py
import random

print("hello world")

"""class3"""
"""
使用type()检查变量的类型
"""

"""
类型转换
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。
"""
a = 100
b = 12.123
c = "hello world"
d = True
print(float(a))
print(int(d))
print(str(b))
print(bool(c))
# 将整数变成对应的字符 (97刚好对应字符表中的字母a)
print(chr(97))
# 将字符转成整数 (Python中字符和字符串表示法相同)
print(ord('a'))
"""
总结：变量用来保存数据，变量具有不同的类型，变量可以用作类型转换
"""

"""class4"""
print("----class4----")
print(321//123)#整除
print(321/123)
print(321%123)#求模（余数）
print(2**3)#求幂
"""
赋值运算和复合赋值运算：将右边的值赋值给左边的变量
"""
a=10
a *= a+2
print(a)
"""比较运算符和逻辑运算符
短路情况：若and左边为false，则右边被跳过；若or左边为True，则右边被跳过
比较运算符优先级高于赋值运算符
"""
flag0 = 1 == 1
print(flag0)

"""print占位符的两种形式：例子，华氏温度转摄氏温度
%.1f是一个占位符，稍后会由一个float类型的变量值替换掉它
{f:.1f}和{c:.1f}可以先看成是{f}和{c}，表示输出时会用变量f和变量c的值替换掉这两个占位符，后面的:.1f表示这是一个浮点数，小数点后保留1位有效数字
"""
# f = float(input('华氏温度：'))
# c = (f - 32) / 1.8
# print('%.1f华氏温度 = %.1f摄氏温度'%(f,c))
# print(f'{f:.1f}华氏温度 = {c:.1f}摄氏温度')

"""class5"""
print("----class5----")
"""分支结构"""
# x = float(input("please input a number:"))
# if x > 1:
#     b = 3 * x - 5
# elif x >= -1 and x <= 1:
#     b = x + 2
# else:
#     b = 5 * x +3
# print(b)

"""class6"""
print("----class6----")
"""循环"""
"""for-in
range(101),0-100整数
range(0,101),0-100整数,前闭后开
range(1,101,2),1-100奇数整数，步长2，每次递增2
range(100,0,-2)，100-1偶数整数，步长-2，每次递减2
"""
total = 0
for x in range(2,101,2):
    total = total + x
print(total)

"""while"""
# num = random.randint(1,100)
# flag = True
# i = 0
# while flag:
#     gus_num = int(input("input random number please:"))
#     if gus_num == num:
#         flag = False
#         print("Righht!!!!!")
#     elif gus_num > num:
#         print("so bigggg!smaller please..")
#     else:
#         print("so smalll!bigger please..")
#     i += 1
# print("u guess %.d times"% i )

"""break & continue
break终止其所在循环，嵌套循环需注意
continue放弃本次循环后续的代码，直接进行下一次循环
"""
# for i in range (1,10):
#     for j in range (1,10):
#         print("%.d * %.d = %.d"%(i,j,i*j),end="   ")
#     print(" ")

for i in range (1,10):
    for j in range (1,i+1):
        print("%.d * %.d = %.d"%(i,j,i*j),end="\t")
    print(" ")

# num = int(input("input a random +number please:"))
# for i in range(2,num):
#     if num%i == 0:
#         print("不是素数")
#         break
#     else:
#         i += 1
#     if(i == num -1):
#         print("是素数")

# print("输入两个正整数，计算他们的最大公约数和最小公倍数")
# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     x, y = y, x    # Python中可以用这样的方式来交换两个变量的值
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print(f'{x}和{y}的最大公约数是{factor}')
#         print(f'{x}和{y}的最小公倍数是{x * y // factor}')
#         break

"""class7"""
print("----class7分支和循环结构的应用----待定")

"""class8"""
print("----class8函数和模块----关于阶乘")
"""
def关键字定义函数，在函数名后面的圆括号中可以放置传递给函数的参数，就是我们刚才说到的函数的自变量，而函数执行完成后我们会通过return关键字来返回函数的执行结果，就是我们刚才说的函数的因变量。
代码重构：在不影响代码执行结果的前提，对代码结构进行调整。
若函数中无return语句，则返回空值None
"""
#输入m，n计算C(m,n)
# m = int(input('m = '))
# n = int(input('n = '))
# # 计算m的阶乘
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# # 计算n的阶乘
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# # 计算m-n的阶乘
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# # 计算C(M,N)的值
# print(fm // fn // fm_n)

#重构上述代码
# def fac(num):
#     result = 1
#     for num in range(1,num+1):
#         result *= num
#     return result
#
# m = int(input('m = '))
# n = int(input('n = '))
#
# print(fac(m) // fac(n) // fac(m - n))
"""参数的默认值
Python中还允许函数的参数拥有默认值,带默认值的参数必须放在不带默认值的参数之后
"""
def add(a,b=0,c=0):
    return a+b+c
print(add(4))
print(add(0,1))
print(add(0,1,2))
# 传递参数时可以不按照设定的顺序进行传递，但是要用“参数名=参数值”的形式
print(add(c=50, a=100, b=200))
"""可变参数
向函数传入0个或任意多个参数，可以通过星号表达式语法来支持可变参数
"""
def add2(*args):
    total = 0
    for val in args:
        total += val
    return total
print(add2(1))
print(add2(3,6))
print(add2())
"""用模块管理函数
Python中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候我们通过import关键字导入指定的模块再使用完全限定名的调用方式就可以区分到底要使用的是哪个模块中的foo函数
module1.py
def foo():
    print('hello, world!')
module2.py
def foo():
    print('goodbye, world!')
test.py
import module1
import module2

# 用“模块名.函数名”的方式（完全限定名）调用函数，
module1.foo()    # hello, world!
module2.foo()    # goodbye, world!
-----
用as关键字对模块进行别名
import module1 as m1
import module2 as m2
---
test.py
from module1 import foo
foo()    # hello, world!
from module2 import foo
foo()    # goodbye, world
会造成覆盖
test.py
from module1 import foo as f1
from module2 import foo as f2
f1()    # hello, world!
f2()    # goodbye, world!
"""
"""标准库中的模块和函数"""
"""总结：函数是功能相对独立且会重复使用的代码的封装"""

"""class9"""
print("----class9常用数据结构之字符串----more")
"""字符串：由零个或多个字符组成的有限序列
以三个双引号或单引号开头的字符串可以拆行
print函数中的end=''表示输出以后不换行，即将默认的结束符\n（换行符）更换为''（空字符）
"""
s1 = 'hello'
s2 = "world"
print(s1,s2)
s3 = """
hello,
world!
"""
print(s3)
"""转义字符和原始字符串
可以在字符串中使用\（反斜杠）来表示转义，也就是说\后面的字符不再是它原来的意义，所以如果字符串本身又包含了'、"、\这些特殊的字符，必须要通过\进行转义处理
Python中的字符串可以r或R开头，这种字符串被称为原始字符串，意思是字符串中的每个字符都是它本来的含义，没有所谓的转义字符
Python中还允许在\后面还可以跟一个八进制或者十六进制数来表示字符,在\\u后面跟Unicode字符编码
"""
s1 = '\'hello world\''
print(s1)
s2 = '\\hello world\\'
print(s2)
s1 = '\time up \now'
s2 = r'\time up \now'
print(s1)
print(s2)
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1,s2)

"""
字符串的运算
"""
"""拼接和重复 + *"""
s1 = 'hello' + ' ' + 'world!'
s2 = '!' * 3
print(s1 + s2)
s1 += s2
print(s1)
s1 *= 2
print(s1)
"""比较运算，直接使用比较运算符比较两个字符串的相等性或大小，比较的是字符串的内容:而'boy' < 'bad'，因为第一个字符都是'b'比不出大小，所以实际比较的是第二个字符的大小"""
s1 = 'Young and rich'
s2 = 'Young and poor'
print(s1 == s2, s1 < s2)
print(s1 == 'Young and rich')
print(s1 == 'young and rich')
s3 = '江饵'
print(ord('江'),ord('饵'))
s4 = '姜肆'
print(ord('姜'),ord('肆'))
print(s3 > s4, s3 <= s4)
"""is运算符（身份运算符），如果用is来比较两个字符串，它比较的是两个变量对应的字符串是否在内存中相同的位置（内存地址）"""
s1 = 'Young and rich'
s2 = 'Young and rich'
s3 = s2
print(s1 == s2, s3 == s2)
print(s1 is s2, s2 is s3)#True True ???
"""成员运算用in和not in判断一个字符串中是否存在另外一个字符或字符串"""
s4 = 'rich'
s5 = 'Rich'
print(s4 in s1, s5 in s1, s5 not in s1)
"""获取长度"""
print(len('Young and rich'))#14
"""索引和切片"""
"""索引
[n]n是整数，假设长度为N，则正向索引，n取0至N-1，0为第一个字符索引；逆向索引，n取-1至-N。字符串为不可变类型，则不能通过索引运算修改字符串中的字符。
若索引越界（超出0至N-1或-N至-1范围），会引发IndexError
"""
print(s1[0],s1[13],s1[-1],s1[-14],s1[4])
"""切片
[i:j:k]，i为开始索引，索引对应的字符可以取到；j为结束索引，索引对应的字符不可取到，k是步长，默认为1
k>0，正向切片（前往后），i默认0，j默认N；k<0，逆向切片（后往前），i默认为-1，j默认为-N-1
索引和切片：对索引而言，索引最大or最小值与切片相差1，因切片取不到最大or最小的那个值
"""
s1 = '1234567'
print(s1[0:7])
print(s1[-1:-8:-1])
print(s1[::])
print(s1[1::2])
print(s1[0:8:2])
print(s1[-1:-8:-1])
print(s1[0:7:1])
"""
循环遍历
"""
for ch in s1:
    print(ch)
for index in range(len(s1)):
    print(s1[index])
"""
字符串的方法：变量名.方法名()
"""
"""大小写相关操作"""
s1 = 'young and rich'
print(s1.capitalize())#Young and rich
print(s1.title())#Young And Rich
print(s1.upper())#YOUNG AND RICH
print(s1.upper().lower())#young and rich
"""查找操作
在一个字符串中寻找是否有另一个字符串，find或index方法，rfind或rindex逆寻找。
find找到返回索引值，否则-1；index找到返回索引值，找不到引发异常
还可以制定索引位置开始寻找，默认为0
"""
s1 = 'young and rich'
print(s1.find('nd'))
print(s1.find('he'))
print(s1.index('nd'))
# print(s1.index('he'))#异常：substring not found
print(s1.find('n'))#从前往后找n第一次出现位置
print(s1.find('n',4))#从索引位置4开始查找n出现的位置
print(s1.rfind('n'))#从后往前找n第一次出现，即n最后一次出现位置
"""性质判断
startwith、endwith判断字符串是否以某个字母开始、结束
is开头的方法判断字符串的特征，以上均返回bool值
"""
s1 = 'young and rich'
print(s1.startswith('y'))#True
print(s1.startswith('o'))#False
print(s1.endswith('h'))#True
print(s1.endswith('o'))#False
print(s1.islower())#True 是否是小写
print(s1.isdigit())#False 是否是数字构成
print(s1.isalpha())#True 是否是字母构成-->False 存在空格
"""格式化字符串
center、ljust、rjust->居中、左对齐、右对齐
print输出字符串是，三种方式进行格式化;3.6,以f打头的字符串中，{变量名}是一个占位符，会被变量对应的值将其替换掉
https://pic3.zhimg.com/v2-ac152392d0ee6c7790ade320122aa8ee_r.jpg
"""
s1 = 'young and rich'
print(s1.center(20,'*'))#以宽度为20将字符串居中，并在两侧填充*
print(s1.rjust(20))#宽度20右对齐，左侧填充空格
print(s1.ljust(20,'~'))#宽度20左对齐，右侧填充~
print('33'.zfill(5))#左侧补0
print('-11'.zfill(5))
a = 12
b = 10
print('%d * %d = %d'%(a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')
"""修剪操作
strip、lstrip、rstrip修剪字符串两端空格
"""
s1 = '    young and rich   '
print(s1)
print(s1.strip())
print(s1.rstrip())
print(s1.lstrip())
"""替换操作
replace（替换的内容，替换后的内容，替换的次数）默认全部替换
"""
s1 = 'young and rich'
print(s1.replace('n','$'))
print(s1.replace('n','$',1))
"""拆分/合并操作
split(指定按照什么来拆分（默认空格)，拆分次数）,将一个字符串拆分为多个字符串（放在一个列表中）
join将列表中的多个字符串连接成一个字符串
"""
s1 = 'young and rich'
s2 = 'young^and^rich'
print(s1.split())
print('*'.join(s1.split()))
print(s2.split('^'))
print(s2.split('^', 1))
"""编码/解码操作
表示二进制数据的字节串类型（bytes）。所谓字节串，就是由零个或多个字节组成的有限序列。
字符串的encode方法，我们可以按照某种编码方式将字符串编码为字节串，我们也可以使用字节串的decode方法，将字节串解码为字符串
"""
a = '江饵'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b, c)
print(b.decode('utf-8'))
print(c.decode('gbk'))
print(b.decode('gbk'))#乱码
"""字符串匹配检查
re 正则表达式，检查字符串是否满足某种特定模式
"""
"""----class10----字符串应用"""
print('----class10----')
# TODO(Yong):字符串应用

"""----clas1s1----列表：list 数据结构"""
print("class11".center(21,"-"))
"""定义和使用
列表是由一系元素按特定顺序构成的数据序列，可以保存多个数据，而且允许有重复的数据
使用[]字面量语法来定义列表，列表中的多个元素用逗号进行分隔;Python内置的list函数将其他序列变成列表,创建列表对象的构造器
列表是一种可变数据类型，也就是说列表可以添加元素、删除元素、更新元素。字符串是一种不可变数据类型，也就是说对字符串做拼接、重复、转换大小写、修剪空格等操作的时候会产生新的字符串，原来的字符串并没有发生任何改变
"""
item1 = [12, 56, 67, 345, 45]
print(item1)
item2 = ['young', 'and', 'rich']
print(item2)
item1 = list(range(1,10))
print(item1)
item2 = list('young and rich')
print(item2)
"""列表的运算符
拼接、重复、成员运算、索引、切片、比较运算
索引、切片越界问题与字符串类似，不同的是，列表可通过索引操作更新列表中的元素
"""
item1 = list('young and')
item2 = list(' rich')
print(item1 + item2)
print(item2 * 4)
print('old' in item1)#False
print('y' in item1)#True
size = len(item1)
print(f"size = {size}")
print("size = %d"%(size))
print("size = {0}".format(size))
print(item1[0],item1[size - 1])
print(item1[::], item1[::-1], item1[3:], item1[:6], item1[-2:-6:-1])
item1 = [1, 2, 3, 4]
item2 = list(range(5))
print(item1 == item2)
print(item1 is item2)
item3 = [4, 5, 6]
print(item1 <= item3)
"""遍历"""
item1 = list('young and rich')
for item in item1:
    print(item)
for index in range(len(item1)):
    print(item1[index])
#掷色子统计每个点数出现次数6000次
import  random
counter = [0] * 6
for i in range(6000):
    face = random.randint(1,6)
    counter[face - 1] += 1
for face in range(1, 7):
    print(f'点数{face}出现{counter[face - 1]}次')
"""列表方法"""
"""添加删除
append()末尾添加；insert（索引位置，‘’）；
remove（指定元素）删除指定元素（元素不再，异常ValueError）；
pop（索引位置）删除指定索引位置（越界，异常IndexError）
claer()清空
"""
item1 = ['Young', 'Rich', 'Too', 'simple', 'hard']
item1.append('kaycee')
print(item1)
item1.insert(2, 'Sit')
print(item1)
item1.remove('hard')
print(item1)
item1.pop(3)
print(item1)
del item1[1]#与pop无实质性区别，性能略差
print(item1)
item1.clear()
print(item1)
"""元素位置和次数
index查找某个元素在列表中的索引位置，第二个参数指从哪个位置开始寻找
count统计一个元素中列表中的出现次数
"""
item1 = ['Young', 'Rich', 'Rich', 'simple', 'Young']
print(item1.index('Young'))
print(item1.index('Young', 2))
# #Rich存在列表中，但从索引位置3开始之后不在出现，
# print(item1.index('Rich', 4))#'Rich' is not in list
print(item1.count('Young'))
print(item1.count('Rich'))
print(item1.count('simple'))
"""元素排序与反转
sort、reverse
"""
item1 = [11, 45, 1, 5, 78, 102]
item1.sort()
print(item1)
item1.reverse()
print(item1)
"""生成式创建列表"""
# 创建一个由1到9的数字构成的列表
items1 = []
for x in range(1, 10):
    items1.append(x)
print(items1)

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = []
for x in 'hello world':
    if x not in ' aeiou':
        items2.append(x)
print(items2)

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = []
for x in 'ABC':
    for y in '12':
        items3.append(x + y)
print(items3)
#对应生成式
item1 = [x for x in range(1, 11)]
print(item1)
item2 = [x for x in 'hello world' if x not in ' aeiou']
print(item2)
item3 = [x + y for x in 'ABC' for y in '12']
print(item3)
"""嵌套的列表
不能用[[0] * 3] * 5]
https://pic1.zhimg.com/v2-912f0d98b55da63f7e98257dabd02c18_b.jpg
"""
score = [[0] * 3] * 5
score[0][0] = 95
print(score)

score = [[0] * 3 for _ in range(5)]
score[0][0] = 95
print(score)
"""总结
列表底层是一个可以动态扩容的数组，列表元素在内存中也是连续存储的，所以可以实现随机访问（通过一个有效的索引获取到对应的元素且操作时间与列表元素个数无关）
列表是容器，可以保存各种类型的数据，可以通过索引操作列表元素
"""

"""----class11元组----"""
print('元祖'.center(20, '-'))
"""定义和使用
元祖是不可变类型，常用（）字面量语法，支持运算符和列表相同
定义、索引、遍历、成员、拼接、切片、比较
"""
t1 = ('young', 18, 'fe', 'china')
t2 = ('blue', 18, 'ET')

t1_le = len(t1)
t2_le = len(t2)
print(t1[0], t1[t1_le-1], t1[-1], t1[-t1_le])
for tu in t2:
    print(tu)
print('blue' in t1)
print('young' in t1)
t3 = t1 + t2
print(t3)
print(t2[::], t2[0:t2_le:2], t2[-1:-4:-1])
print(t1 > t2)
"""一个元祖有几个元素称几元组，（）表示空元祖，元祖中只有一个元素，则需加逗号，如（1，）"""
t1 = ()
print(type(t1))
t1 = ('hello')
print(type(t1))
t1 = ('hello',)
print(type(t1))
"""元素应用"""
"""打包解包
如果解包出来的元素个数和变量个数不对应，会引发ValueError异常，错误信息为：too many values to unpack（解包的值太多）或not enough values to unpack（解包的值不足）
可使用星号表达式修饰该表量，使其变成列表接收多个值（列表中有0个或多个元素）。在解包语法中*只能出现一次。
"""
a = (1, 2, 'hello') #打包
i, j, k = a #解包
print(a, i, j, k)
# i, j = a #ValueError: too many values to unpack (expected 2)
# i, j, k, f = a #ValueError: not enough values to unpack (expected 4, got 3)
a = (1, 10, 100, 1000)
i, j, *k = a # 1 10 [100, 1000]
print(i, j, k)
i, *j, k = a # 1 [10, 100] 1000
print(i, j, k)
*i, j, k = a # [1, 10] 100 1000
print(i, j, k)
i, j, k, *l = a# 1 10 100 [1000]
print(i, j, k, l)
i, j, k, l, *m = a # 1 10 100 1000 []
print(i, j, k, l, m)
"""解包语法对所有序列都成立，含字符串、列表、元祖"""
a, *b, c = range(10) #0 [1, 2, 3, 4, 5, 6, 7, 8] 9
print(a, b, c)
a, b, c = [1, 10, 100] #1 10 100
print(a, b, c)
a, *b, c = 'hello' #h ['e', 'l', 'l'] o
print(a, b, c)
"""函数的可变参数就是将多个参数打包成一个元祖"""
def add(*args):
    print(type(args), args)
    total = 0
    for tu in args:
        total += tu
    return total
print(add(1, 2, 3))
"""交换两个变量的值
下列并没用到打包解包语法
"""
a, b, c = [1, 2, 3]
print(a, b, c)
a, b, c = c, b, a
print(a, b, c)
"""元祖类型可让函数返回多个值"""
def find_max_min(items):
    max_one, min_one = items[0], items[0]
    for item in items:
        if item > max_one:
            max_one = item
        elif item < min_one:
            min_one = item
    return max_one, min_one
print(find_max_min((12, 65, 3, 76, 87, 100, -453)))
"""元祖与列表
元组是不可变类型，不可变类型更适合多线程环境，因为它降低了并发访问变量的同步化开销
元组是不可变类型，通常不可变类型在创建时间和占用空间上面都优于对应的可变类型:使用sys模块的getsizeof函数来检查保存相同元素的元组和列表各自占用了多少内存空间。我们也可以使用timeit模块的timeit函数来看看创建保存相同元素的元组和列表各自花费的时间
Python中的元组和列表是可以相互转换的
列表是可变数据类型，元组是不可变数据类型，所以列表添加元素、删除元素、清空、排序等方法对于元组来说是不成立的。但是列表和元组都可以进行拼接、成员运算、索引和切片这些操作
"""
import sys
import  timeit
a = list(range(100000))
b = tuple(range(100000))
print(sys.getsizeof(a), sys.getsizeof(b))
print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))
a = ['young', 145, 'china', True]
b = ('app', 'lee', 'opp')
print(list(b))
print(tuple(a))

a = 1723.28+6.33+1.84+26641.58+1120.51+35000+10374.42+4534.68+902.01+124.34
print(a)
"""class21"""

























