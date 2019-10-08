# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:51:45 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/4f356b0618d14737a6f3782771bb4079?tpId=90&tqId=30798&tPage=2&rp=2&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
牛牛举办了一场数字游戏,有n个玩家参加这个游戏,游戏开始每个玩家选定一个数,然后将这个数写在纸上(十进制数,无前缀零),然后接下来对于每一个数字将其数位按照非递减顺序排列,得到新的数,新数的前缀零将被忽略。得到最大数字的玩家赢得这个游戏。

输入：输入包括两行,第一行包括一个整数n(1 ≤ n ≤ 50),即玩家的人数
第二行n个整数x[i](0 ≤ x[i] ≤ 100000),即每个玩家写下的整数。
输出：输出一个整数,表示赢得游戏的那个玩家获得的最大数字是多少。

eg:
输入：3
9638 8210 331

3689
输出：3689
"""
n = int(input().strip())
num = list(input().strip().split())

#print(num[0][0])

new_num = []
for i in range(len(num)):
    tmp = []
    for j in range(len(num[i])):
        if num[i][j] != '0':
            tmp.append(int(num[i][j]))
    tmp.sort()
    for n in range(len(tmp)):
        tmp[n] = str(tmp[n])
    new_num.append(int("".join(tmp)))

print(max(new_num))