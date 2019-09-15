# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 01:47:14 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/ab900f183e054c6d8769f2df977223b5?tpId=90&tqId=30789&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
牛牛又从生物科研工作者那里获得一个任务,这次牛牛需要帮助科研工作者从DNA序列s中找出最短没有出现在DNA序列s中的DNA片段的长度。
例如:s = AGGTCTA
序列中包含了所有长度为1的('A','C','G','T')片段,但是长度为2的没有全部包含,例如序列中不包含"AA",所以输出2。

输入：输入包括一个字符串s,字符串长度length(1 ≤ length ≤ 2000),其中只包含'A','C','G','T'这四种字符
输出：输出一个正整数,即最短没有出现在DNA序列s中的DNA片段的长度。

eg:
AGGTCTA
2

"""
s = input().strip()
#print(len(s))
for i in range(6):
    if 4**i <= len(s) <4**(i+1):
        k = i+1
        
        
tmp_1 = []
for j in range(k):
    tmp = []
    for m in range(len(s)-j):
        tmp.append(s[m:m+j+1])
    se = set(tmp)
    if len(se) < 4**(j+1):
        tmp_1.append(j+1)
    
print(tmp_1[0])