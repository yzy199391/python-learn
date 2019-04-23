# -*- coding: utf-8 -*-
def my_pow(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 为参数指定默认值。
# ⚠️ 默认参数在后，必选参数在前
# ⚠️ 变化大的参数在前，变化小的参数在后。变化小的参数可以作为默认参数
# 使用默认参数，大大简化参数调用
def my_pow2(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
if __name__ == '__main__':
    print(my_pow(2, 10))
    print(my_pow2(2))
    print(my_pow2(2, 10))