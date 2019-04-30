#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'carl.yan'

# 动态语言"鸭子类型"：一个对象只要看起来像鸭子，走起路来像鸭子，它就可以被看作是鸭子
# 以Animal类为例，其作为父类，有多个子类继承它；动态语言在需要传入Animal时，不一定需要传入Animal类型。只需要保证传入的对象有一个run()方法即可

class Animal():
    def run(self):
        print("animal is running")

class Dog(Animal):
    def run(self):
        print("dog is running")

class Cat(Animal):
    def run(self):
        print("cat is running")

def run_twice(animal):
    animal.run()
    animal.run()

class FileLike(object):
    def run(self):
        print("file-like object is running")

if __name__ == '__main__':
    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())
    # 动态语言传入对象只要实现了run方法即可
    run_twice(FileLike())

