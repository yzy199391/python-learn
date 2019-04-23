# -*- coding: utf-8 -*-
list = ["Michael", "Bob", "Tracy"]
listNum = range(101)

if __name__ == '__main__':
    for name in list:
        print(name)

    sum = 0
    for num in listNum:
        sum = sum + num
    print(sum)

    for num in range(101):
        sum = sum + num
    print(sum)

    n = 99
    sum = 0
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)

    # break 强制跳出循环
    n = 1
    while n <= 100:
        if n > 10:
            break
        print(n)
        n = n + 1
    print("END")

    # continue 跳过当前循环
    n = 0
    while n < 10:
        n = n + 1
        if n % 2 == 0:
            continue
        print(n)
    print("END")


    # 练习
    L = ['Bart', 'Lisa', 'Adam']
    for name in L:
        print("Hello, %s!" % name)
if __name__ == '__main__':

    # 死循环
    i = 0
    while i <= 0:
        i = i - 1
        print("循环中...")






