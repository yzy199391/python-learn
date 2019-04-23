# -*- coding: utf-8 -*-
import math

if __name__ == "__main__":
    a = input("please insert an integer: ")
    int = int(a)
    if int >= 0:
        print("输入了一个正整数：{0}".format(int))
    elif int < 0 and int >= -10:
        print("输入了一个-10 ～ 0之间的整数：{0}".format(int))
    else:
        print("输入了一个小于-10的整数：{0}".format(int))

    # 练习
    height = 1.75
    weight = 80.5
    bmi = weight / (math.pow(height, 2))

    if bmi <= 18.5:
        print("过轻")
    elif bmi > 18.5 and bmi <= 25:
        print("正常")
    elif bmi > 25 and bmi <= 28:
        print("过重")
    elif bmi > 28 and bmi <=32:
        print("肥胖")
    else:
        print("严重肥胖")

    
