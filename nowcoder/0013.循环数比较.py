# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 01:28:08 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/24575008c6134b6fa4fab8ea0ea82a99?tpId=90&tqId=30788&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
对于任意两个正整数x和k,我们定义repeat(x, k)为将x重复写k次形成的数,例如repeat(1234, 3) = 123412341234,repeat(20,2) = 2020.
牛牛现在给出4个整数x1, k1, x2, k2, 其中v1 = (x1, k1), v2 = (x2, k2),请你来比较v1和v2的大小。

输入：输入包括一行,一行中有4个正整数x1, k1, x2, k2(1 ≤ x1,x2 ≤ 10^9, 1 ≤ k1,k2 ≤ 50),以空格分割
输出：如果v1小于v2输出"Less",v1等于v2输出"Equal",v1大于v2输出"Greater".
eg:
1010 3 101010 2
Equal
"""
x1,k1,x2,k2 = input().strip().split()

k1 = int(k1)
k2 = int(k2)
v1 = x1*k1 
v2 = x2*k2
tmp = []
index = []

#1 greater 2 less 3 equal
def len_equal(v1,v2):
    if len(v1) == len(v2):
        for i in range(len(v1)):
            if int(v1[i])>int(v2[i]):
                tmp.append(1)
            elif int(v1[i])<int(v2[i]):
                tmp.append(2)
            else:
                tmp.append(0)
    if max(tmp) == 0:
        return 0
    else:
        for j in range(len(tmp)):
            if tmp[j] != 0:
                return tmp[j]
                break
            
            
            
if len(v1) > len(v2):
    print("Greater")
elif len(v1) < len(v2):
    print("Less")
else:
    if len_equal(v1,v2) == 0:
        print("Equal")
    elif len_equal(v1,v2) == 1:
        print("Greater")
    else:
        print("Less")