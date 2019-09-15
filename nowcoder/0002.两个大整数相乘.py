# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:37:14 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/0f0badf5f2204a6bb968b0955a82779e?tpId=90&tqId=30777&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
有两个用字符串表示的非常大的大整数,算出他们的乘积，也是用字符串表示。不能用系统自带的大整数类型。

输入：空格分隔的两个字符串，代表输入的两个大整数
输出：输入的乘积，用字符串表示

eg:
72106547548473106236 982161082972751393
70820244829634538040848656466105986748
"""

num = list(map(int,input().strip().split()))
print(str(num[0]*num[1]))
