# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:32:15 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/c4ea1f2263434861aef111aa44a5b064?tpId=90&tqId=30791&tPage=1&rp=1&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
牛牛有一个由小写字母组成的字符串s,在s中可能有一些字母重复出现。比如在"banana"中,字母'a'和字母'n'分别出现了三次和两次。
但是牛牛不喜欢重复。对于同一个字母,他只想保留第一次出现并删除掉后面出现的字母。请帮助牛牛完成对s的操作。

输入：输入包括一个字符串s,s的长度length(1 ≤ length ≤ 1000),s中的每个字符都是小写的英文字母('a' - 'z')
输出：输出一个字符串,表示满足牛牛要求的字符串

eg:
banana
ban

"""
s = list(input().strip())
#print(s)

new_s = []
for word in s:
    if word not in new_s:
        new_s.append(word)

print("".join(new_s))