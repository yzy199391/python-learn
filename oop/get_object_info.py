#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types

__author__ = 'carl.yan'

def func():
    print("this is a function")

class Animal():
    def run(self):
        print("animal is running")

class Dog(Animal):
    def run(self):
        print("dog is running")

    def __len__(self):
        return 100

class Student():
    # 类属性
    name = "Student"

if __name__ == '__main__':
    # type()判断对象类型：
    ## 基本数据类型都可以判断
    print(type(123))
    print(type("str"))
    print(type(None))

    ## 指向函数或类的变量，也可以判断
    print(type(abs))

    ## type()返回对应的Class类型
    print("类型比较：%s" % (type(123) == type(456)))
    print(type(123) == int)
    print(type(123) == type("str"))

    # types()判断一个对象是否是函数
    print("内建函数：%s" % (type(abs) == types.BuiltinFunctionType))
    print("func 是一个函数类型对象：%s" % (type(func) == types.FunctionType))
    print("lambda 类型：%s" % (type(lambda x: x) == types.LambdaType))
    print("generator 类型：%s" % (type((x for x in range(1, 11))) == types.GeneratorType))

    # instance()判断class类型，适用于继承场景
    d = Dog()
    print("dog继承是Animal的实例：%s" % (isinstance(d, Animal)))
    ## 判断一个变量是否为某些类型中的一种
    print("变量是list和tuple中的一种： %s" % (isinstance([1, 2, 3], (list, tuple))))

    # dir()获取对象所有属性和方法，返回一个包含字符串的list
    print(dir(str))
    ## __xxx__格式的属性和方法在python中都有特殊用途；如调用len()，其内部实现是自动取调用对象的__len__()方法
    print("str".__len__() == len("str"))
    print(len(d))
    ## 判断对象是否包含指定属性、获取属性、设置属性
    ##若无属性，返回默认值
    print(getattr(d, "name", "pipi"))
    print("Dog class has \"name\" attribute：%s" % hasattr(d, "name"))
    print("Dog class has \"run()\" attribute：%s" % hasattr(d, "run"))

    # 实例属性与类属性
    # ⚠️：不要将实例属性与类属性设置相同名字，因为此时实例属性会屏蔽掉类属性
    s = Student()
    print("实例属性name为：%s" % s.name)
    print("类属性name为：%s" % s.name)

    s.name = "Carl"
    print("实例属性name为：%s" % s.name)
    print("类属性name为：%s" % s.name)

    # 删除实例属性后，访问的是同名的类属性
    del s.name
    print(s.name)








