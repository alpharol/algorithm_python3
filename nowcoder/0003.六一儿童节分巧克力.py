# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:43:47 2019

@author: Mr.Reliable
"""

#https://www.nowcoder.com/practice/d2dfc62bf1ba42679a0e358c57da9828?tpId=90&tqId=30778&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking

"""
六一儿童节，老师带了很多好吃的巧克力到幼儿园。
每块巧克力j的重量为w[j]，对于每个小朋友i，当他分到的巧克力大小达到h[i] (即w[j]>=h[i])，他才会上去表演节目。
老师的目标是将巧克力分发给孩子们，使得最多的小孩上台表演。
可以保证每个w[i]> 0且不能将多块巧克力分给一个孩子或将一块分给多个孩子。

输入：第一行：n，表示h数组元素个数
     第二行：n个h数组元素
     第三行：m，表示w数组元素个数
     第四行：m个w数组元素
 
输出：上台表演学生人数

eg:
输入： 3 
     2 2 3
     2
     3 1 
 
输出：1
"""

n = int(input().strip())
n_num = list(map(int,input().strip().split()))   #孩子的要求
m = int(input().strip())
m_num = list(map(int,input().strip().split()))   #老师的巧克力

n_num.sort(reverse=True)   #对孩子的要求从大到小排序
m_num.sort(reverse=True)   #老师巧克力从大到小排序


count = 0
for i in range(len(m_num)):
    for j in range(len(n_num)):
        if m_num[i]>=n_num[j]:
            count = count + 1
            n_num = n_num[j+1:]
            break

print(count)