# -*- coding: utf-8 -*-
# 声明, dict类似java中map
d = {"Carl" : 100, "Michael" : 95, "Tracy" : 90}

# 声明, set
s = set([1, 1, 2, 2, 3])

if __name__ == '__main__':
    print(d["Carl"])

    # dict中新增元素
    d["Tom"] = 85
    print(d["Tom"])

    # 通过d[]方式获取dictionary内值，若key不存在抛出异常；通过get()方法获取指定值，若key不存在，返回None或自己指定的value
    print(d.get("b"))
    print(d.get("a", -404))

    # 移除
    d.pop("Tom")
    print(d.get("Tom"))

    s.add(4)
    print(s)

    # 随机移除一个元素
    s.pop()
    print(s)

    #移除指定元素
    s.remove(3)
    print(s)
