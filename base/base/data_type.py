if __name__ == "__main__":
    print("\\\n\\")
    # r""默认后续字符串不开启转义
    print(r"\\\n\\")

    # 输入多行内容
    print('''line1
line2
line3''')
    print(r'''hello,\n
world''')

    # boolean
    print(True and True)
    print(False or True)
    print(2 > 5)

    # None 等价于java中的 Null
    print(None)

    # 声明变量
    a = 1
    b = False
    c = 'carl'
    print(a, b, c)
    # 动态语言特性，定义变量无需指定变量类型；java是静态语言
    a = 'A'
    print(a)

    print(10 / 3)
    # 地板除，向下取整
    print(10 // 3)
    print(20 // 3)
    # 取余
    print(10 % 3)

