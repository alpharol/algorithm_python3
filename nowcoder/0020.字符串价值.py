# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 01:37:36 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/9240357eefcf4d938b90bdd5eec3712b?tpId=90&tqId=30795&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
有一种有趣的字符串价值计算方式:统计字符串中每种字符出现的次数,然后求所有字符次数的平方和作为字符串的价值
例如: 字符串"abacaba",里面包括4个'a',2个'b',1个'c',于是这个字符串的价值为4 * 4 + 2 * 2 + 1 * 1 = 21
牛牛有一个字符串s,并且允许你从s中移除最多k个字符,你的目标是让得到的字符串的价值最小。

输入：输入包括两行,第一行一个字符串s,字符串s的长度length(1 ≤ length ≤ 50),其中只包含小写字母('a'-'z')。
第二行包含一个整数k(0 ≤ k ≤ length),即允许移除的字符个数。
输出：输出一个整数,表示得到的最小价值

eg:
aba
1

2
"""

###关键在于每次都对最大的数减1.
s = input().strip()
k = int(input().strip())

a = list(set(s))
num = []
for i in range(len(a)):
    num.append(s.count(a[i]))

num.sort(reverse=True)

for j in range(k):
    num[0] = num[0]-1
    num.sort()

m=0
for n in num:
    m = m + n**2

print(m)

