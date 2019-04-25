# -*- coding: utf-8 -*-

def get_new_list(origL):
    newL = []
    for i in range(0, len(origL)) :
        if i == 0:
            newL.append(1)
        else:
            newL.append(origL[i - 1] + origL[i])
    newL.append(1)
    return newL

def yh_triangle():
    l1 = [1]
    while True:
        yield l1
        l1 = get_new_list(l1)



if __name__ == '__main__':
    L = get_new_list([1, 2, 1])
    print(L)

    n = 0
    g = yh_triangle()
    for i in g:
        print(i)
        n += 1
        if n > 10:
            break