# -*- coding: utf-8 -*-
# generator：为了节省空间，可以在创建list时，不一次性创建完整的列表，而是一边循环一边计算后续元素。
# 链表
def split(name):
    print("----------------%s--------------------" % name)

# 普通函数打印斐波那契数列前n项
def fib(n):
    i = 0
    e1, e2 = 0, 1
    while i < n:
        print(e2)
        e1, e2 = e2, e1 + e2
        i = i + 1
    return "done"

# 创建斐波那契数列前n项组成的generator
# ⚠️包含yield的函数是一个generator
def fib_g(n):
    i = 0
    e1, e2 = 0, 1
    while i < n:
        yield e2
        e1, e2 = e2, e1 + e2
        i = i + 1
    return "done"

# 函数中的yiled返回计算出的generator的下一个值，函数返回一个generator
def g_process():
    print("step 1")
    yield 1
    yield 3
    print("step 2")
    print("step 3")
    yield 5

# 练习
# 杨辉三角,方式1
def get_new_list(origL):
    newL = []
    for i in range(0, len(origL)) :
        if i == 0:
            newL.append(1)
        else:
            newL.append(origL[i - 1] + origL[i])
    newL.append(1)
    return newL

def yh_triangle():
    origL = [1]
    while True:
        yield origL
        origL = get_new_list(origL)

# 杨辉三角, 方式2
def yh_triangle2():
    origL = [1]
    while True:
        yield origL
        origL = [origL[x - 1] + origL[x] for x in range(1, len(origL))]
        origL.insert(0, 1)
        origL.append(1)

if __name__ == '__main__':
    # 创建generator，只需将列表生成式的[]改为()
    split("创建并打印generator")
    g = (x for x in range(1, 10))
    print("获取generator中下一个元素：%s %s" % (next(g), next(g)))

    for i in g:
        print(i)

    split("普通函数打印斐波那契数列")
    print(fib(5))
    split("打印斐波那契数列generator")
    for i in fib_g(10):
        print(i)

    split("generator执行流程")
    g = g_process()
    next(g)

    split("杨辉三角练习，方式1")
    n = 0
    g = yh_triangle()
    for i in g:
        print(i)
        n += 1
        if n > 10:
            break

    split("杨辉三角练习，方式2")
    n2 = 0
    g2 = yh_triangle2()
    for j in g2:
        print(j)
        n2 += 1
        if n2 > 10:
            break



