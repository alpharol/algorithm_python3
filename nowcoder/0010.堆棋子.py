#https://www.nowcoder.com/practice/27f3672f17f94a289f3de86b69f8a25b?tpId=90&tqId=30785&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking
"""
小易将n个棋子摆放在一张无限大的棋盘上。第i个棋子放在第x[i]行y[i]列。
同一个格子允许放置多个棋子。每一次操作小易可以把一个棋子拿起并将其移动到原格子的上、下、左、右的任意一个格子中。
小易想知道要让棋盘上出现有一个格子中至少有i(1 ≤ i ≤ n)个棋子所需要的最少操作次数.

输入：输入包括三行,第一行一个整数n(1 ≤ n ≤ 50),表示棋子的个数
第二行为n个棋子的横坐标x[i](1 ≤ x[i] ≤ 10^9)
第三行为n个棋子的纵坐标y[i](1 ≤ y[i] ≤ 10^9)

输出：输出n个整数,第i个表示棋盘上有一个格子至少有i个棋子所需要的操作数,以空格分割。行末无空格

如样例所示:
对于1个棋子: 不需要操作
对于2个棋子: 将前两个棋子放在(1, 1)中
对于3个棋子: 将前三个棋子放在(2, 1)中
对于4个棋子: 将所有棋子都放在(3, 1)中


输入样例：4
1 2 4 9
1 1 1 1

输出：0 1 3 10
"""


n = int(input().strip())
heng = list(map(int,input().strip().split()))
zong = list(map(int,input().strip().split()))

"""
问题的关键在于：最后最优聚合点的横纵坐标都必须在给定点的集合内
"""
set_heng=list(set(heng))
set_zong=list(set(zong))

pri = [[0]*1 for _ in range(n)]

for i in range(len(set_heng)):
    for j in range(len(set_zong)):  #i*j个候选点（候选最优集合点）
        tmp = []
        for k in range(n):      #对于每一个点计算n个原始点到它的距离
            tmp.append(abs(heng[k]-set_heng[i])+abs(set_zong[j]-zong[k]))
        tmp.sort()  #排序
        for m in range(n):
            pri[m].append(sum(tmp[:(m+1)]))
     
wait = []
for p in range(n):
    pri[p]=pri[p][1:]
    wait.append(min(pri[p]))

wait = list(map(lambda x:str(x),wait))
print(" ".join(wait))  