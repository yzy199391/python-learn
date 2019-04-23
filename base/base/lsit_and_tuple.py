# -*- coding: utf-8 -*-
if __name__ == "__main__":
    # list

    # 初始化
    list = [1, 2, 3]
    print(list[0])
    # 获取元素个数
    print(len(list))
    # 倒序取元素
    print(list[-1])
    print(list[-3])
    # 追加元素到末尾
    list.append(4)
    print(len(list))
    print(list[-1])
    #元素插入指定位置
    list.insert(1, 5)
    print(list)
    # 删除末尾元素
    list.pop()
    print(list)
    # 删除指定位置元素
    list.pop(1)
    print(list)
    # 替换指定元素-直接为指定元素赋值
    list[1] = 4
    print(list)
    # list中可存放不同类型元素
    list.append("string1")
    print(list)
    list2 = [5,6,7]
    list.append(list2)
    print(list)
    # 获取二维数组中的指定值
    print(list[4][1])

    # tuple 元组，一旦初始化，则无法修改
    #初始化
    tuple = (1, 2, 3)
    # ⚠️定义只有一个元素的tuple必须加逗号，否则默认按小括号计算而非初始化tuple算
    tuple2 = (1,)
    print(tuple2)

    # "可变tuple"
    list=["str1", "str2", "str3"]
    tuple = (1, 2, list)
    tuple[2][0] = "new_str_1"
    print(tuple)


    # 实例
    L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
    ]
    ## 打印Apple
    print(L[0][0])
    ## 打印Python
    print(L[1][1])
    ## 打印Lisa
    print(L[2][2])
