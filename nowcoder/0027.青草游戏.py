#https://www.nowcoder.com/practice/ed0334a5e88f4662bb69374b308862d8?tpId=90&tqId=30802&tPage=2&rp=2&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
牛牛和羊羊都很喜欢青草。今天他们决定玩青草游戏。
最初有一个装有n份青草的箱子,牛牛和羊羊依次进行,牛牛先开始。
在每个回合中,每个玩家必须吃一些箱子中的青草,所吃的青草份数必须是4的x次幂,比如1,4,16,64等等。
不能在箱子中吃到有效份数青草的玩家落败。假定牛牛和羊羊都是按照最佳方法进行游戏,请输出胜利者的名字。

输入:输入包括t+1行。
第一行包括一个整数t(1 ≤ t ≤ 100),表示情况数.
接下来t行每行一个n(1 ≤ n ≤ 10^9),表示青草份数
输出:对于每一个n,如果牛牛胜利输出"niu",如果羊羊胜利输出"yang"。

eg： 
输入：
3
1
2
3

输出：niu
yang
niu
"""

###这道题目的关键在于找规律，否则的话一定会超时
"""
方法1：1个循环
"""
n=int(input().strip())
for i in range(n):
    x = int(input().strip())
    if x%5 in [1,3,4]:
        print("niu")
    else:
        print("yang")
		
		
"""
方法2：2个循环
"""
n=int(input().strip())
num = []
for i in range(n):
    x = int(input().strip())
	num.append(x)
	
for j in range(n):
    if num[j]%5 in [1,3,4]:
        print("niu")
    else:
        print("yang")
		
		
"""
方法3：好多循环,这个就超时了！
"""
n=int(input().strip())
num = []
for i in range(n):
    x = int(input().strip())
    num.append(x)

def cha(a):
    k=0
    while(a!=0):
        for j in range(14):
			if 4**j <= a <4**(j+1):
                a = a-4**j
                k=k+1
                break                
    return int(k)
	
for m in range(n):
        if cha(num[m])%2==0:
                print("yang")
        else:
                print("niu")