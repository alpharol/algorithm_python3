# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:47:57 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/e11bc3a213d24fc1989b21a7c8b50c3f?tpId=90&tqId=30781&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
如果一个数列S满足对于所有的合法的i,都有S[i + 1] = S[i] + d, 这里的d也可以是负数和零,我们就称数列S为等差数列。
小易现在有一个长度为n的数列x,小易想把x变为一个等差数列。
小易允许在数列上做交换任意两个位置的数值的操作,并且交换操作允许交换多次。
但是有些数列通过交换还是不能变成等差数列,小易需要判别一个数列是否能通过交换操作变成等差数列

输出：输入包括两行,第一行包含整数n(2 ≤ n ≤ 50),即数列的长度。
第二行n个元素x[i](0 ≤ x[i] ≤ 1000),即数列中的每个整数。
输入：如果可以变成等差数列输出"Possible",否则输出"Impossible"。

eg:
3
3 1 2

Possible
"""

n = int(input().strip())
num = list(map(int,input().strip().split()))
#从大到小排序
num.sort(reverse = True)

gap = (num[-1]-num[0])/(len(num)-1)

tmp = []
for i in range(len(num)-1):
    if num[i]+gap == num[i+1]:
        tmp.append(1)
    else:
        tmp.append(0)

if min(tmp) == 0:
    print("Impossible")
else:
    print("Possible")