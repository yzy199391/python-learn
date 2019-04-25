# -*- coding: utf-8 -*-
L = [1, 2, 3, 4, 5, 6]
L2 = list(range(100))

t = (1, 2, 3, 4,5)

# 练习
# 去除字符串首尾一个空格
def trim(s):
    if s[0] == " " and s[-1] == " ":
        s = s[1 : -1]
    elif s[1] == " ":
        s = s[1 : ]
    elif s[-1] == " ":
        s = s[: -1]
    else:
        s = s[:]
    return s

# 去除首尾所有空格
def adv_trim(s):
    i = 0
    j = -1
    start = 0
    end = 0
    while s[i].isspace():
        i = i + 1
        start = i

    while s[j].isspace():
        j = j - 1
        end = j
    return s[start : end + 1]


if __name__ == '__main__':
    # 从索引0找到索引2
    print(L[: 3])
    # 从索引1找到索引2
    print(L[1 : 3])
    # 倒序，从倒数第二个找到结尾
    print(L[-2 : ])

    # 前10个数，每2个取一个
    print(L2[: 10 : 2])

    # 所有数字，每5个取1个
    print(L2[: : 5])

    # 复制list
    print(L[:])

    # tuple
    print(t[: 3])

    print(trim(" abc "))
    print(adv_trim("     abcd e f     "))




