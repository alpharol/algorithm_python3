#https://www.nowcoder.com/practice/5f29c72b1ae14d92b9c3fa03a037ac5f?tpId=90&tqId=30776&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking

"""
给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大，
要求时间复杂度：O(n)，空间复杂度：O(1)

输入：无序整数数组A[n]   
输出：满足条件的最大乘积  

eg:
3 4 1 2

24
"""

n = int(input().strip())
#一行中每一列都变成int然后存在list中
l = list(map(int,input().strip().split()))

#a用来存储前三个最大值
#b用来存储两个最小值
a,b=[],[]
#l_1和l_2复制两次，因为需要删除元素
l_1,l_2 = l[:],l[:]


###核心思想在于最大的三个正数或者最小的两个负数和最大的正数
def maxi(l):
    if len(l)<3:
        return "wrong"
    elif len(l)==3:
        return l[0]*l[1]*l[2]
    else:
        for i in range(3):
            k1 = max(l_1)
            a.append(k1)
            l_1.remove(k1)
        for j in range(2):
            k2 = min(l_2)
            b.append(k2)
            l_2.remove(k2)
    return max(a[0]*a[1]*a[2],a[0]*b[0]*b[1])
    

print(maxi(l))