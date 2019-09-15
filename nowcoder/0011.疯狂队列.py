#https://www.nowcoder.com/practice/d996665fbd5e41f89c8d280f84968ee1?tpId=90&tqId=30786&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking

"""
小易老师是非常严厉的,它会要求所有学生在进入教室前都排成一列,并且他要求学生按照身高不递减的顺序排列。
有一次,n个学生在列队的时候,小易老师正好去卫生间了。
学生们终于有机会反击了,于是学生们决定来一次疯狂的队列,
他们定义一个队列的疯狂值为每对相邻排列学生身高差的绝对值总和。
由于按照身高顺序排列的队列的疯狂值是最小的,他们当然决定按照疯狂值最大的顺序来进行列队。
现在给出n个学生的身高,请计算出这些学生列队的最大可能的疯狂值。小易老师回来一定会气得半死。

输入：输入包括两行,第一行一个整数n(1 ≤ n ≤ 50),表示学生的人数
第二行为n个整数h[i](1 ≤ h[i] ≤ 1000),表示每个学生的身高
输出：输出一个整数,表示n个学生列队可以获得的最大的疯狂值。

如样例所示: 
当队列排列顺序是: 25-10-40-5-25, 身高差绝对值的总和为15+30+35+20=100。
这是最大的疯狂值了。

eg:
5
5 10 25 40 25

100
"""  

n=int(input().strip())
num=list(map(int,input().strip().split()))

list_1 = []
for i in range(int(n/2)):
    max_1 = max(num)
    min_1 = min(num)
    if i == 0:
        list_1.append(min_1)
        list_1.append(max_1)
        num.remove(max_1)
        num.remove(min_1)
    else:
        if list_1[0]-list_1[1]<0:
            list_1.insert(0,max_1)
            list_1.append(min_1)
            num.remove(max_1)
            num.remove(min_1)
        else:
            list_1.append(max_1)
            list_1.insert(0,min_1)
            num.remove(max_1)
            num.remove(min_1)

if len(num) == 0:
    pass
else:
    if abs(num[0]-list_1[0])>abs(num[0]-list_1[-1]):
        list_1.insert(0,num[0])
    else:
        list_1.append(num[0])

sum_1 = 0

for j in range(n-1):
    sum_1 = sum_1+abs(list_1[j+1]-list_1[j])

print(sum_1)
