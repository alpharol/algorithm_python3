# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 00:19:53 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/b53bda356a494154b6411d80380295f5?tpId=90&tqId=30783&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking

"""
小易有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
1、将a_i放入b序列的末尾
2、逆置b序列
小易需要你计算输出操作n次之后的b序列。

输出：输入包括两行,第一行包括一个整数n(2 ≤ n ≤ 2*10^5),即序列的长度。
第二行包括n个整数a_i(1 ≤ a_i ≤ 10^9),即序列a中的每个整数,以空格分割。
输入：在一行中输出操作n次之后的b序列,以空格分割,行末无空格。


eg：
4
1 2 3 4

4 2 1 3
"""
#这个不可以用循环，时间复杂度高
n = int(input().strip())
num = list(input().strip().split())

b = []

if n%2 == 0:
    b = num[-1:0:-2]+num[0:n-1:2]
    print(" ".join(b))
else:
    b = num[-1:0:-2]+[num[0]]+num[1:n:2]
    print(" ".join(b))