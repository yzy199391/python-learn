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

# 闭包：内部函数对外部函数参数进行引用：def f(n): def infunc(x): retrun pow(x, n) return infunc
# 上述中f生命周期结束，已经引用的变量n存在在infunc中，依然可以调用；⚠️由于上述原因，尽量避免在闭包中引用循环变量或者后续会发生变化的变量
# 下例中，count()返回为列表其内部f()函数；
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

# 闭包使用后续变化了的变量，下述外部传入值为1时，调用内部函数，结果为121，即为变化后的值被内部函数引用计算后的结果
def error_exp(i_out):
    def infunc(i_in):
        return pow(i_out, i_in)
    i_out += 10
    return infunc

# 若要引用循环变量，用如下方式
def cycle_count():
    fs = []
    def in_f(i):
        def in_g():
            return i * i
        return in_g
    for i in range(1, 4):
        fs.append(in_f(i)) # f(i)被立即执行，因此i的当前值被传入f()
    return fs

# 练习，计数器
def create_counter():
    def increase():
        i = 0
        while True:
            i += 1
            yield i

    it = increase() # 此步骤重要

    def counter():
        return next(it)
    return counter


if __name__ == '__main__':
    split("调用返回函数")
    f = lazy_sum(1, 2, 3, 4)
    print(f())

    # 每次调用返回函数都会创建一个新函数，计算结果互不影响
    split("-")
    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print(f1 == f2)

    split("闭包局部参数特性")
    # count生命周期结束时，i值变为3，内部函数引用其值即为3。但内部函数并未立即执行，直到如下调用时开始执行，所以下述结果都为9
    f1, f2, f3 = count()
    print("f1 计算结果为：%s" % f1())
    print("f2 计算结果为：%s" % f2())
    print("f3 计算结果为：%s" % f3())

    f1 = error_exp(1)
    print(f1(2))

    f1, f2, f3 = cycle_count()
    print("f1 计算结果为：%s" % f1())
    print("f2 计算结果为：%s" % f2())
    print("f3 计算结果为：%s" % f3())

    counterA = create_counter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())