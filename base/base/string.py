# pythen解释器读取源代码时，下面一行代码让它按utf-8编码读取。⚠️在文本编辑器中正在使用UTF-8 without BOM编码
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    # 支持多种语言
    print("包含中文的str")

    # order()获取字符的整数表示
    print(ord('A'))
    print(ord('中'))

    # chr()将编码转换为对应字符
    print(chr(65))
    print(chr(20013))

    # 字符整数编码
    print("\u4e2d\u6587")

    # bytes类型数据 b""
    print(b'ABC')

    # encode()将str编码为指定bytes
    print("ABC".encode("ascii"))
    print("中文".encode("utf-8"))
    # decode()将bytes解码为str
    print(b"ABC".decode("ascii"))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))
    # 若bytes中只有一小部分无效字节，可以传入errors='ignore'忽略错误字节
    print(b'\xe4\xb8\xad\xff'.decode("utf-8", errors="ignore"))
    # len()计算str包含多少个字符
    print("ABC 字符数：", len("ABC"))
    print("\"中文\" 字符数：", len("中文"))
    # len()计算bytes的字节数
    print("ABC 字节数：", len(b"ABC"))
    print("\"中文\" 字节数", len(b"\xe4\xb8\xad\xe6\x96\x87"))
    print("\"中文\" 字节数", len("中文".encode("utf-8")))

    # 格式化字符串
    print("占位符替换str, %s, %s" % ("world", "a"))
    print("占位符替换整数, %d, %d" % (1, 2))
    print("占位符替换浮点数, %f" % 1.0)
    print("占位符替换十六进制整数, %x" % 0x100F)
    # 指定是否补0和整数与小数的位数
    print("指定是否补0, %2d - %02d" % (3, 1))
    print("指定浮点小数位数, %.4f" % 3.1415926)
    # %s永远有效，可将任何类型转换为str
    print("整数：%s, 浮点：%s" % (1, 2.0))
    # %%转义表示%，只有在str中包含%占位符时会生效
    print("%%%% 转义表示 %%, %d" % 5)

    # format()格式化str，使用{0}、{1}...
    print("整数：{0}, 浮点数：{1:.1f}".format(1, 1.224))

    # 实例
    s1 = 72
    s2 = 75
    percent = (s2-s1) / s1 * 100
    integerPart = int(percent)
    decimalPart = round((percent - integerPart) * 100 / 10)

    if percent >= 10:
        print("小明成绩提升的百分点是：%.1f%%" % percent)
    else:
        print("小明成绩提升的百分点是：%02d.%d %%" % (integerPart, decimalPart))



