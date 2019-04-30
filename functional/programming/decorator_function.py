# -*- coding: utf-8 -*-

# 装饰器：接收一个函数作为参数，并返回一个参数
# 调用： 可以借助python的@语法置于函数的定义处
import functools
import time


def log(func):
    @functools.wraps(func) # 防止装饰后函数名变为wrapper
    def wrapper(* args, **kw):
        print("call %s():" % func.__name__)
        return func(* args, **kw)
    return wrapper

@log # 等价于执行 now = log(now)
def now():
    print("2019-4-28")

# decorator本身需要传入参数
def log(text):
    def decorator(func):
        def wrapper(* args, **wk):
            print("%s %s(): " % (text, func.__name__))
            return func(* args, **wk)
        return wrapper
    return decorator

@log("testText")
def now2():
    print("2019-4-28")

# 练习
def decorator_time(func):
    @functools.wraps(func)
    def wrapper(* args, **wk):
        start_time = time.time()
        r = func(* args, **wk)
        print("%s executed in %s ms" % (func.__name__, 1000 * (time.time() - start_time)))
        return r
    return wrapper

@decorator_time
def fast(x, y):
    time.sleep(0.0012)
    return x + y

if __name__ == '__main__':
    now()
    print(now.__name__)
    now2()
    print(now2.__name__)
    r = fast(11, 22)
    print(r)
