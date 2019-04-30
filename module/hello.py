#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 任何模块代码的第一个字符串都被视为模块的文档注释
'a test module'

# 作者
__author__ = 'carl.yan'

# 引入sys模块
import  sys

def test():
    # 用list存储命令行所有参数，argv至少有一个元素，第一个参数永远是该.py文件的名称
    args = sys.argv
    if len(args) == 1:
        print("Hello, World!")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("Too many arguments!")