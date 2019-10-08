#https://www.nowcoder.com/practice/fae8632cfc64433989720bc01e09f382?tpId=90&tqId=30806&tPage=2&rp=2&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
牛牛选择了一个正整数X,然后把它写在黑板上。然后每一天他会擦掉当前数字的最后一位,直到他擦掉所有数位。 在整个过程中,牛牛会把所有在黑板上出现过的数字记录下来,然后求出他们的总和sum.
例如X = 509, 在黑板上出现过的数字依次是509, 50, 5, 他们的和就是564.
牛牛现在给出一个sum,牛牛想让你求出一个正整数X经过上述过程的结果是sum.

输入描述:
输入包括正整数sum(1 ≤ sum ≤ 10^18)
输出描述:
输出一个正整数,即满足条件的X,如果没有这样的X,输出-1。

eg:
输入:564
输出:509
"""

"""
解题思路：首先如果给的数字是4位的，那么组成它的数字至少是3或4位的。用1000*a+100*b+10*c+d来表示。在表示好了之后，还要看一下
结果是不是可以组成原来的数字，这里看的方法就是最后一位数是不是10以下的，如果不是的话，那就不能表示。
"""
n = int(input().strip())
str_n = str(n)

tmp = []
for i in range(len(str_n)):
    ones = int("1"*(len(str_n)-i))   #组成几个1的数字
    if (n//ones) < 10:
        tmp.append(n//ones)
        n = n - (n//ones)*int("1"*(len(str_n)-i))   #为后面判断是否可行做准备
    else:
        break

num = ""
if len(tmp) != len(str_n):
    print(-1)
else:
    if tmp[0] != 0:
        for t in tmp:
            num = num + str(t)
        print(int(num))
    else:
        for t in tmp[1:]:
            num = num + str(t)
        print(int(num))




