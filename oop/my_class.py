#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'carl.yan'

# 类定义括号内可以放此类继承的父类； 所有类内函数与普通函数区别为：其第一个参数必定为self，调用时无需传入。
class Student():
    # 特殊变量，可以直接访问
    __static__ = "static variable"
    # 虽然可以被访问，但视为私有变量，不随意访问
    _private_tatic = "private static"

    def __init__(self, name, score, age, gender):
        self.name = name
        self.score = score
        # 私有变量，以__开头,无法从外部访问
        self.__age = age
        self.__gender = gender

    def get_age(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    # 练习 隐藏gender参数，用 get/set 替代，检查参数有效性
    def get_gender(self):
        return
if __name__ == '__main__':
    carl = Student("carl", 90, 12, "male")
    print(carl.score)

    # ⚠️：动态语言允许对实例变量绑定任何数据
    lisa = Student("lisa", 80, 15, "female")

    lisa.weight = 180

    print(lisa.weight)
    # print(carl.weight)

    # 测试私有变量
    # print(carl.__age)
    # 通过get方法获取私有变量
    print(carl.get_age())
    # 通过解释器转换获取私有变量
    # ⚠️：不同版本的python解释器可能会把__name改成不同的变量名
    print(carl._Student__age)

    print(carl.__static__)

    # print(carl._private_tatic)



