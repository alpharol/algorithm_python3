# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:50:08 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/cc929a2ed85f4f49b834e6e301fba77b?tpId=90&tqId=30792&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
牛牛有羊羊有了属于他们自己的飞机。于是他们进行几次连续的飞行。f[i]表示第i次飞行所需的燃油的升数。飞行只能按照f数组所描述的顺序进行。
起初飞机里有s升燃油,为了正常飞行,每次飞行前飞机内燃油量应大于等于此处飞行所需要的燃油量。请帮助他们计算在不进行加油的情况下他们能进行的飞行次数。

输入:输入包括两行,第一行包括两个整数n和s(1 ≤ n ≤ 50, 1 ≤ s ≤ 1000),分别表示计划飞行的次数和飞起初始状态下有的燃油量。
第二行包括n个整数f[i], (1 ≤ f[i] ≤ 1000), 表示每次计划飞行所需要的燃油量。
输出:输出一个整数,表示他们能进行的飞行次数。

eg：
7 10
1 2 3 4 5 6 7

4
"""
n,s = map(int,input().strip().split())
oil = list(map(int,input().strip().split()))


if sum(oil) <= s:
    print(n)
else:
    for i in range(n):
        if sum(oil[:i+1])>s:
            print(i)
            break