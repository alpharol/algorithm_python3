# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:29:56 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/d9f5dbd3b57d450e8406e102573d4bdd?tpId=90&tqId=30800&tPage=2&rp=2&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking


"""
牛牛手中有三根木棍,长度分别是a,b,c。牛牛可以把任一一根木棍长度削短,牛牛的目标是让这三根木棍构成一个三角形,并且牛牛还希望这个三角形的周长越大越好。

输入：输入包括一行,一行中有正整数a, b, c(1 ≤ a, b, c ≤ 100), 以空格分割
输出：输出一个整数,表示能拼凑出的周长最大的三角形。


eg:
1 2 3

5
"""
num = list(map(int,input().strip().split()))

num.sort()

if num[0]+num[1] > num[2]:
    print(sum(num))
else:
    print(2*num[0]+2*num[1]-1)