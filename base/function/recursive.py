# -*- coding: utf-8 -*-
# 计算阶乘
def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)

def fac2(n):
    return fac_iter(n, 1)
# 尾递归
def fac_iter(num, product):
    if num == 1:
        return product
    return fac_iter(num - 1, num * product)

# 练习 汉诺塔 将a上n个盘子，全部移动到c
# 把n个盘子，借助b，从a移动到c
def move(n, a, b, c):
    # 若a只有一个盘子，直接从a移动到c
    if n == 1:
        print('move', a, '-->', c)
    else:
        # 首先将n-1个盘子借助c，从a移动到b
        move(n-1, a, c, b)
        # 将剩下到盘子借助b从a移动到c
        move(1, a, b, c)
        # 将移动到b到n-1个盘子借助a从b移动到c
        move(n-1, b, a, c)

if __name__ == '__main__':
    print(fac(7))
    print(move(5, 'A', 'B', 'C'))
