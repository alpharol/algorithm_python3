# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 01:50:01 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/826c2f28ee2a414cac87eb0304eca1a0?tpId=90&tqId=30797&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
牛牛的老师给出了一个区间的定义:对于x ≤ y,[x, y]表示x到y之间(包括x和y)的所有连续整数集合。例如[3,3] = {3}, [4,7] = {4,5,6,7}.牛牛现在有一个长度为n的递增序列,牛牛想知道需要多少个区间并起来等于这个序列。
例如:
{1,2,3,4,5,6,7,8,9,10}最少只需要[1,10]这一个区间
{1,3,5,6,7}最少只需要[1,1],[3,3],[5,7]这三个区间

输入：输入包括两行,第一行一个整数n(1 ≤ n ≤ 50),
第二行n个整数a[i](1 ≤ a[i] ≤ 50),表示牛牛的序列,保证序列是递增的。
输出：输出一个整数,表示最少区间个数。

输入：5
1 3 5 6 7
输出
3
"""
n = int(input().strip())
li = list(map(int,input().strip().split()))

k=0
for i in range(n-1):
    if li[i]+1 != li[i+1]:
        k=k+1

print(k+1)
