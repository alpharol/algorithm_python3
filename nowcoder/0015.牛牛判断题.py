# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:20:48 2019

@author: Mr.Reliable
"""
##https://www.nowcoder.com/practice/ce5b35929ab84e3a806886d9667be00a?tpId=90&tqId=30790&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking

"""
牛牛参加了一场考试,考试包括n道判断题,每做对一道题获得1分,牛牛考试前完全没有准备,所以考试只能看缘分了,
牛牛在考试中一共猜测了t道题目的答案是"正确",其他的牛牛猜为"错误"。
考试结束后牛牛知道实际上n道题中有a个题目的答案应该是"正确",但是牛牛不知道具体是哪些题目,
牛牛希望你能帮助他计算可能获得的最高的考试分数是多少。

输入：输入包括一行,一行中有三个正整数n, t, a(1 ≤ n, t, a ≤ 50), 以空格分割
输出：输出一个整数,表示牛牛可能获得的最高分是多少。

eg:
3 1 2
2
"""

n,t,a = map(int,input().strip().split())

if t == a:
    print(n)
elif t < a:
    print(t+n-a)
else:
    print(a+n-t)