#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/23 22:37
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'

"""
对list的随机访问

随机访问就是指能不能通过下标之类的索引直接访问某一位置的元素。数据结构中，顺序表最主要的特点就是随机访问。

python中list的索引只能是整数或者切片。

通过整数访问就和一些高级编程语言中的数组的访问类似，直接通过中括号里面加整数下标。但python中整数下标是支持负数下标的，负数表示从list最后一个元素开始计算，如-2就是指list的倒数第二个元素，其他的以此类推。

通过切片访问，要知道切片的书写格式
[start:end:det]
start表示起点，end表示终点，det表示访问时下标每次的增量，即步长。

如果det值为1，那么实际上就是获取list对象中下标在[start, end)之间的所有元素(注意，这是数学上的左闭右开区间)。
对于det属于任意非0整数的情况，实际上就是获取list对象中下标分别是
start start+det start+det*2 …… start+det*i
的元素构成的新列表，其中|start+det*i| < |end|，且i∈N，注意双竖线||表示取里面的绝对值，因为考虑到负数下标的问题。

和一些高级编程语言中函数的参数列表中的默认参数类似，这里的变量也有默认值，默认情况下start是0，end是整个list的长度，det是1，所以我们也应该遵守相关使用默认参数的规则，如果某一个参数不使用默认参数，那么其前面的参数也都不是之前所说的默认值，所以在python中表现就是可以只用1个冒号，也可以用2个冒号。

    ls = [1, 2, 3]#创建一个包含1,2,3三个元素的list
    print(ls)#输出整个ls对象
    print(ls[0], ls[1], ls[2])#按整数下标的方式输出ls上的每一个元素
    print(ls[-3], ls[-2], ls[-1])#通过负下标的方式从按序输出ls上的每一个元素
    print(ls[0:])#通过切片的方式，将下标从0开始到最后一个元素的切片输出，当然如果是输出整个ls的话‘0’可以省略
    print(ls[-1::-1])#通过切片的方式，将下标从-1开始到第一个元素的切片输出，当然如果是逆序输出整个ls的话，第一个‘-1’可以省略

输出：
[1, 2, 3]
1 2 3
1 2 3
[1, 2, 3]
[3, 2, 1]
如何“弹出”list的第一个和最后一个元素

先不谈list的内置方法，结合之前学过的list的访问，我们最先想到的可能就是先取到指定位置元素的值，然后再通过del方法删除该位置上的元素。

示例如下：

    ls = [1, 2, 3]
    print(ls)#删除之前的ls
    val = ls[0]
    del(ls[0])
    print(val)#输出第一个元素的值
    print(ls)#输出修改后的ls

输出：
[1, 2, 3]
1
[2, 3]

很明显，过程比较麻烦，需要先取再删。而在我们学习编程和数据结构的过程，会发现很多高级编程语言都会有pop函数，这个函数就是用来完成上述功能。

同样的，python中list对象也为我们内置了pop函数，其接收一个整数表示需要获取的元素的下标，且支持负数下标，不使用参数，则默认弹出最后一个元素。

示例如下：

    ls = [1, 2, 3]
    print(ls)#删除之前的ls
    val = ls.pop(-1)#如果是获取最后一个元素的值，此处的`-1`可省略
    print(val)#输出最后一个元素的值
    print(ls)#输出修改后的ls
    val = ls.pop(0)
    print(val)#输出第一个元素的值
    print(ls)#输出修改后的ls

输出：
[1, 2, 3]
3
[1, 2]
1
[2]
如何向list添加数据

我们先在ipython的命令行窗口看看list到底有哪些函数可以为我们所用。

list对象的方法

看了上图，大家可以尝试猜一下这些函数的功能，上图中list的这些函数在很多其他高级编程语言都有类似函数，可以说是非常通用且强大。这里，从英语上来说，append和extend都具有“添加”的意思，那为什么要分两个呢，让我们先来实验一下。

示例如下：

    ls = [1, 2, 3]
    print(ls)
    ls.append([4, 5, 6])
    print(ls)#输出通过append函数修改后的ls
    ls.extend([4, 5, 6])
    print(ls)#输出通过extend函数修改后的ls

输出：
[1, 2, 3]
[1, 2, 3, [4, 5, 6]]
[1, 2, 3, [4, 5, 6], 4, 5, 6]

通过上述例子可以看到，append函数是把参数直接原封不动地添加到ls对象的尾部，而extend函数是把参数中的元素提取出来，然后再添加到ls对象的尾部，所以大家在用的时候要视情况选择正确的函数。

更简便的是，类似与一些高级编程语言中的运算符重载，python中list对象之间的+操作可以实现类似extend函数的功能。

示例如下：

    ls = [1, 2, 3]
    print(ls)
    ls = ls + [4, 5, 6]
    print(ls)#输出通过append函数修改后的ls

输出：
[1, 2, 3]
[1, 2, 3, 4, 5, 6]
编程要求

根据提示，在右侧编辑器补充代码，先将输入的list添加4,5,6 3个元素，再添加元素[7,8,9]，计算并输出修改后的list，及其第一个和最后一个元素。

本关涉及的代码文件为src/step1/hello_world_stu.py，请读者仔细阅读并完成空缺代码的填写。
测试说明

本关的测试文件是src/step1/hello_world_stu.py。

    读者将 src/step1/hello_world_stu.py 中的代码补充完毕，然后点击评测，平台自动编译运行 src/step1/hello_world_stu.py，并以标准输入方式提供测评输入；
    平台获取程序的输出，然后将其与预期输出对比，如果一致则测试通过；否则测试失败。

我会对你编写的代码进行测试：

测试输入：
1,2,3,4,5
预期输出：
[1, 2, 3, 4, 5, 4, 5, 6, [7, 8, 9]]
1
[7, 8, 9]
"""
ls = list(map(lambda x: int(x), input().split(',')))

# 请在此添加代码，实现将修改后的list、队首元素和队尾元素输出
# ********** Begin *********#
ls2 = [4, 5, 6]
ls3 = [7, 8, 9]
ls.extend(ls2)
ls.append(ls3)
print(ls)
print(ls[0])
print(ls[-1])
# #********** End **********#
