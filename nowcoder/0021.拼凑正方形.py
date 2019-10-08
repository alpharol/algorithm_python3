# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 01:42:59 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/563c6a69fd714e59a942d97047cedcb3?tpId=90&tqId=30796&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
牛牛有4根木棍,长度分别为a,b,c,d。羊羊家提供改变木棍长度的服务,如果牛牛支付一个硬币就可以让一根木棍的长度加一或者减一。牛牛需要用这四根木棍拼凑一个正方形出来,牛牛最少需要支付多少硬币才能让这四根木棍拼凑出正方形。


输入：输入包括一行,四个整数a,b,c,d(1 ≤ a,b,c,d ≤ 10^6), 以空格分割
输出：输出一个整数,表示牛牛最少需要支付的硬币

eg：
4 1 5 4

4

"""
s = list(map(int,input().strip().split()))
s.sort()

k1 = s[3]-s[1]+s[2]-s[0]

print(k1)