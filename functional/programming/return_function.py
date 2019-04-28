# -*- coding: utf-8 -*-
def split(name):
    print("----------------%s--------------------" % name)

# 高阶函数返回值可以是一个函数(闭包)
def lazy_sum(*args):
    def sum():
        x = 0
        for n in args:
            x = x + n
        return x
    return sum
if __name__ == '__main__':
    split("调用返回函数")
    f = lazy_sum(1, 2, 3, 4)
    print(f())
    