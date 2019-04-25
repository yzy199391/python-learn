# -*- coding: utf-8 -*-
import os

def split(name):
    print("----------------%s--------------------" % name)

if __name__ == '__main__':
    # 循环生成1～10的平方值组成的数组
    L = []
    for i in range(1, 11):
        L.append(i * i)
    print(L)

    # 列表生成式生成上述list
    L = [i * i for i in range(1, 11)]
    print(L)

    # 上述生成时加筛选条件(下例为筛选偶数)
    L = [i * i for i in range(1, 11) if i % 2 == 0]
    print(L)

    # 使用两层循环
    L = [i + j for i in "ABC" for j in "XYZ"]
    print(L)

    # 列出当前目录下所有文件和目录名
    L = [f for f in os.listdir('.')]
    print(L)

    # 列表生成式用两个变量生成list
    dict = {"K1" : "V1", "K2" : "V2", "K3" : "V3"}
    L = [k + "=" + v for k, v in dict.items()]
    print(L)

    # list中所有字符串变成小写
    L = ["HELLO", "WORLD", "CARL"]
    print([s.lower() for s in L])

    # 练习
    # 列表生成式筛选出所有字符串并转化为小写
    split("练习")
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [x.lower() for x in L1 if isinstance(x, str)]

    # 迭代将所有字符串转为小写
    i = 0
    for x in L1:
        if isinstance(x, str):
            L1[i] = x.lower()
        i = i + 1
    print(L1)