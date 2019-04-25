# -*- coding: utf-8 -*-

from collections import Iterable

dict = {"a" : 1, "b" : 2, "c" : 3, "d" : 4}
str = "abcd"
def split(name):
    print("----------------%s--------------------" % name)

# 练习
# 查找一个list中的最小和最大值
def findMinAndMax(L):
    min = L[0]
    max = L[0]
    for value in L:
        if value > max:
            max = value
        if value < min:
            min = value
    return min, max




if __name__ == '__main__':
    # 迭代dict中key
    split("iterate dict key")
    for key in dict:
        print(dict[key])
    # 迭代dict中value
    split("iterate dict value")
    for value in dict.values():
        print(value)
    # 迭代dict中key、value
    split("iterate dict key and value")
    i = 0
    for key, value in dict.items():
        print("key %d is : %s" % (i, key))
        print("value %d is : %d" % (i, value))
        i = i + 1

    # 迭代字符串
    split("iterate string")
    for ch in str:
        print(ch)

    # 判断一个对象是否可迭代
    split("is iterable")
    print(isinstance("abc", Iterable))
    print(isinstance([1, 2, 3], Iterable))
    print(isinstance(1, Iterable))

    # enumerate()将list变为索引-元素树
    split("list 下标循环")
    for i, value in enumerate(["A", "B", 'C']):
        print(i, value)

    split("for循环中同时引用多个变量")
    for x, y in [(0, 1), (1, 1), (2, 1)]:
        print(x, y)

    # 练习
    split("练习: 查找list中最下最大值")
    min, max = findMinAndMax([1, 2, 3, 5, 6])
    print("最小值为：%s, 最大值为：%s。" % (min, max))

