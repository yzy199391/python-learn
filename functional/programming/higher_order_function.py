# -*- coding: utf-8 -*-
from functools import reduce


def split(name):
    print("----------------%s--------------------" % name)

# 函数接收另外一个函数作为参数，此函数为高阶函数
def add(x, y, f):
    return f(x) + f(y)

def my_pow(x):
    return pow(x, 2)

def square(x, y):
    return x * y

# 将string转换为int的函数
def str2int_tool(x, y):
    return x * 10 + y
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
def str2int(s):
    return reduce(str2int_tool, map(char2num, s))

# lambda简化
def simple_str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# 练习, 名称格式化
def format(s):
    return str.upper(s[0]) + str.lower(s[1 :])
def format_name(l):
    return list(map(format, l))

# 练习, 使用reduce编写求累积函数
def accumulation(l):
    return reduce(lambda x, y: x * y, l)

# 练习, string 转 float
def str2float(s):
    n = s.index(".")
    s1, s2 = list(map(int, s[: n])), list(map(int, s[n + 1 :]))
    print(s1 + s2)
    return reduce(lambda x, y: x * 10 + y, s1 + s2)/(pow(10, len(s1 + s2) - n))

# 序列中只保留非空内容
def not_empty(s):
    return s and s.strip()

# 求素数
## 埃氏筛法：
## 列出2开始所有自然数，筛选去除第一个数2的倍数(获取所有奇数)
## 取新序列第一个数3，筛选去除3的倍数
## 不断重复，就能得到所有素数

# 获取所有奇数序列
def odd_iter():
    n = 1
    while True:
        n += 2
        yield n
# 判断当前数是否可被序列最开始选择的数值整除
def not_divisible(n):
    return lambda x: x % n > 0

# 获取素数generator：输出序列第一位的数，通过之筛选，其必为素数；用第一位的素数筛选当前数组；
def prime_number():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)

# 练习， 获取回文数
def is_palindrome(n):
    i, j = 0, len(n) - 1
    orig = n
    s = 0
    while s < len(orig) // 2:
        if n[0] == n[len(n) - 1]:
            i += 1
            j -= 1
            n = n[i : j + 1]
            s = s + 1
        else:
            return
    return orig

def get_palindrome(n):
    return list(map(int, filter(is_palindrome, list(map(str, n)))))

# 练习：list内元素类型为tuple，按tuple中第一个属性为list排序
def get_name(t):
    return t[0]
def get_grade(t):
    return t[1]

if __name__ == '__main__':
    # 变量指向函数本身，直接调用abs()和f()完全相同
    f = abs
    print(f(-10))

    # abs()的函数名可以看为一个指向函数本身的变量，可以为其赋予其它值，这样会导致函数内容变化
    # abs函数定义在import builtins模块中，所以要让修改abs=10在其它模块也生效，使用 import builtins; builtins.abs = 10
    #abs = 10
    #abs(-10)

    print(add(2, -3, abs))

    # map()函数：参数为  函数 + Iterable；作用为将函数作用到Iterable的每个元素。
    split("map()")
    r = map(my_pow, [x for x in range(1, 11)])
    print(list(r))

    print(list(map(str, [x for x in range(1, 11)])))

    # reduce()函数：reduce(f, [x1, x2, x3, x4]) == f(f(f(x1, x2), x3), x4)
    # ⚠️：reduce()中作为参数的函数必须且只能有两个参数
    print(reduce(square, [2, 2, 2, 2, 2]))

    split("demo: convert string to int")
    print("convert string to int: %d" % str2int('12345'))
    print("convert string to int with simple func: %d" % simple_str2int('12345'))

    split("练习，名称格式化")
    print(format_name(['adam', 'LISA', 'barT']))

    split("练习, 使用reduce编写求累积函数")
    print(accumulation([3, 5 ,7, 9]))

    split("练习, convert string to float")
    print(str2float("124.4563"))

    # filter()函数：参数为 函数 + 序列，返回Iterable；
    # ⚠️：与map区别在于：根据返回值为True还是False决定保留还是丢弃该元素
    split("filter")
    for e in filter(not_empty, ["a", " ", "b", None, "c", "    "]):
        print(e)

    split("primary number")
    i = 0
    for e in prime_number():
        if i > 10:
            break
        print(e)
        i += 1

    split("get palindrome 回文数")
    for e in get_palindrome([x for x in range(1, 200)]):
        print(e)

    split("sorted")
    # python内置sorted()为List排序
    print(sorted([1, -1, 3, 2, 19, 10]))
    # 按传入的key--函数名
    print(sorted([1, -1, 3, 2, 19, 10, -12], key = abs))
    # 字符串排序, 从首位到末尾依次比较ascii码
    print(sorted(["bob", "about", "Zoo", "Zao", "Credit"]))
    # 字符串忽略大小写排序， 实际为全变为大写（或小写）后排序
    print(sorted(["bob", "about", "Zoo", "Zao", "Credit"], key = str.lower))
    # 反向排序, reverse
    print(sorted(["bob", "about", "Zoo", "Zao", "Credit"], key = str.lower, reverse = True))

    # 练习
    split("练习：list[tuple]排序--学生姓名排序")
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key = get_name)
    print(L2)
    split("练习：list[tuple]排序--学生成绩排序，从高到低")
    L3 = sorted(L, key = get_grade, reverse = True)
    print(L3)










