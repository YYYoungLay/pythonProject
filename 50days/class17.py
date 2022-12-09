"""class17 面向对象编程进阶"""
"""可见性和属性装饰器
private __name 
protected _name
public 对象的方法通常是公开的
"""
"""装饰器
property 为私有属性提供读取和修改的方法，通常放在类、函数或方法的声明之前
"""
"""动态属性
在运行时可以改变其结构的语言，例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化
可以动态为对象添加属性，但对象的方法其实本质上也是对象的属性，如果给对象发送一个无法接收的消息，引发的异常仍然是AttributeError
不希望在使用对象时动态的为对象添加属性,可添加’__slots__魔法
"""
class Student:
    # TODO 解决__slots__出现的问题
    # __slots__ = ('name', 'age')#出现许多错误

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f"{self.__name} is studing!")

    #属性访问器（getter方法） - 获取__name属性
    @property
    def name(self):
        return self.__name

    #属性修改器（setter方法） - 修改__name属性
    @name.setter
    def name(self, name):
        #若name参数不为空，则赋值给对象__name属性
        #否则将__name属性赋值为’无名氏‘，有两种方法
        # self.__name = name if name else '无名氏'
        self.__name = name or '无名氏'

    @property
    def age(self):
        return self.__age

stu1 = Student('Blue', 4)
stu1.study('Python')
# print(stu1.__name)#AttributeError 私有属性无法在外直接访问，可更换名字规则进行访问
print(stu1._Student__name, stu1._Student__age)#可在外部访问私有属性

print(stu1.name, stu1.age)
stu1.name = 'Young'
# stu1.age = 3#AttributeError
print(stu1.name, stu1.age)

#为Student对象动态添加sex属性
stu1.sex = 'male'
print(stu1.sex)

"""静态方法和类方法
方法是给对象发送消息的，而这两种给类发送消息
什么消息？调用该方法时，对象还没创建出来
可使用类名.方法名的方式来调用静态方法和类方法，二者的区别在于，类方法的第一个参数是类对象本身，而静态方法则没有这个参数
对象方法、类方法、静态方法都可以通过类名.方法名的方式来调用，区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象。静态方法通常也可以直接写成一个独立的函数，因为它并没有跟特定的对象绑定。
"""
class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形（静态方法）"""
        return a+b > c & a+c > b & b+c > a

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形（类方法）"""
    #     return a+b > c & a+c > b & c+b > a

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5

tri = Triangle(3, 4, 5)
print(tri.perimeter())
print(tri.area())
# print(tri.is_valid())

"""继承和多态
面向对象的编程语言支持在已有类的基础上创建新类，提供继承信息的类叫做父类（超类、基类），得到继承信息的类叫做子类（派生类、衍生类）
继承语法定义类的时候，在类名后的圆括号中指定当前类的父类，允许多重继承。
初始化方法中可通过super().__init__()来调用父类初始化方法，
子类除可以通过继承得到父类提供的属性和方法外，还可以定义自己特有的属性和方法。
在实际开发中，经常会用子类对象去替换一个父类对象，这是面向对象编程中一个常见行为，叫做‘里氏替换原则’
子类继承父类方法后，可对其进行重写，不同子类可对父类的同一个方法给出不同的实现版本，运行时出现多态行为，相同法法，做不同的事
"""
class Person:
    """人类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} eat rice everyday')

class Teacher(Person):
    """老师类"""

    def __init__(self, name, age, title):
        super(Teacher, self).__init__(name, age)
        # super().__init__(name, age)
        self.title = title

    def teach(self):
        print(f'teacher {self.name} teach {self.title}')

teacher = Teacher('wang', 34, 'English')
teacher.teach()
# TODO 里氏替换原则



