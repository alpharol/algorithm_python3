# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 00:58:04 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/e496d8e885a949d18476b2dea1e594a9?tpId=90&tqId=30794&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking
"""
牛牛有一个长度为n的整数序列,牛牛想对这个序列进行重排为一个非严格升序序列。牛牛比较懒惰,他想移动尽量少的数就完成重排,请你帮他计算一下他最少需要移动多少个序列中的元素。(当一个元素不在它原来所在的位置,这个元素就是被移动了的)

输出：输入包括两行,第一行一个整数n(1 ≤ n ≤ 50),即序列的长度
第二行n个整数x[i](1 ≤ x[i] ≤ 100),即序列中的每个数
输入：输出一个整数,即最少需要移动的元素个数

eg：
3
3 2 1

2
"""

n = int(input().strip())
li = list(map(int,input().strip().split()))

a = li[:]

a.sort()
k = 0
for i in range(n):
    if a[i] != li[i]:
        k = k+1
        
print(k)