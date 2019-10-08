# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:24:44 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/4802faa9afb54e458b93ed372e180f5c?tpId=90&tqId=30793&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
如果一个整数只能被1和自己整除,就称这个数是素数。
如果一个数正着反着都是一样,就称为这个数是回文数。例如:6, 66, 606, 6666
如果一个数字既是素数也是回文数,就称这个数是回文素数
牛牛现在给定一个区间[L, R],希望你能求出在这个区间内有多少个回文素数。

输入：输入包括一行,一行中有两个整数(1 ≤ L ≤ R ≤ 1000)
输出：输出一个整数,表示区间内回文素数个数。
"""
L,R = map(int,input().strip().split())

#判断回文数
huiwen = []
for i in range(R-L+1):
    s=str(L+i)
    rev_s = s[::-1]
    if s == rev_s:
        huiwen.append(s)

##复制一遍方便后面remove
huiwen_sushu = huiwen[:]


##判断是否是质数
for j in range(len(huiwen)):
    num = int(huiwen[j])
    for k in range(2,num):
        if num % k == 0:
            huiwen_sushu.remove(str(num))
            break
if L==1:      
    print(len(huiwen_sushu)-1)
else:
    print(len(huiwen_sushu))