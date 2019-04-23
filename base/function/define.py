# -*- coding: utf-8 -*-
import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x

# 空函数
def nop():
    pass

# 返回tuple(省略括号)
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 练习
def quadratic(a, b, c):
    stand = math.pow(b, 2) - 4 * a * c
    if stand >= 0:
        x1 = (-b + math.sqrt(stand)) / (2 * a)
        x2 = (-b - math.sqrt(stand)) / (2 * a)
    else:
        raise RuntimeError("no solution to the quadratic eqution")
    return x1, x2

if __name__ == '__main__':
    print(my_abs(1))
    print(move(1, 2, 3, 90))

    print(quadratic(2, 1, 2))
