# -*- coding: utf-8 -*-

import functools

# 偏函数：functools提供的一个功能；固定函数的某些参数，返回新函数，简化函数调用
def split(name):
    print("----------------%s--------------------" % name)

# 通过设定默认值简化函数调用
def int2(x, base=8):
    return int(x, base)

# 偏函数简化函数调用；重新定义int函数，固定base参数值为8
int3 = functools.partial(int, base = 8)

if __name__ == '__main__':
    print(int2("12345"))
    print(int3("12345"))
