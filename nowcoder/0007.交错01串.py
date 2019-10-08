# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:28:06 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/3fbd8fe929ea4eb3a254c0ed34ac993a?tpId=90&tqId=30782&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
如果一个01串任意两个相邻位置的字符都是不一样的,我们就叫这个01串为交错01串。
例如: "1","10101","0101010"都是交错01串。
小易现在有一个01串s,小易想找出一个最长的连续子串,并且这个子串是一个交错01串。
小易需要你帮帮忙求出最长的这样的子串的长度是多少。


输入：输入包括字符串s,s的长度length(1 ≤ length ≤ 50),字符串中只包含'0'和'1'
输出：输出一个整数,表示最长的满足要求的子串长度。

eg:
111101111
3

"""
s = list(map(int,input().strip()))


###接下来我们设置一个计数器观察他们是不是连续的，并把计数器的每次输出都存在一个list中
k=1
tmp=[]
if len(s)==0:
    print(0)
elif len(s)==1:
    print(1)
else:
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            k=k+1
            tmp.append(k)
        else:
            k=1
            tmp.append(k)

print(max(tmp))