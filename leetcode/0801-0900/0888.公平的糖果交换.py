#https://leetcode-cn.com/problems/fair-candy-swap/

"""
爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 块糖的大小，B[j] 是鲍勃拥有的第 j 块糖的大小。
因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。
（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。
如果有多个答案，你可以返回其中任何一个。保证答案存在。

示例 1：输入：A = [1,1], B = [2,2];输出：[1,2]
示例 2：输入：A = [1,2], B = [2,3];输出：[1,2]
示例 3：输入：A = [2], B = [1,3];输出：[2,3]
示例 4：输入：A = [1,2,5], B = [2,4];输出：[5,4]
"""
###这也超出了时间限制？？？
"""
class Solution:
    def fairCandySwap(self, A: list, B: list):
        tmp = (sum(A)+sum(B))/2
        cha = int(sum(A)-tmp)
        ans = []
        for a in A:
            if (a-cha) in B:
                return [a,a-cha]
"""

###这个题目。。。不难，但是这个时间真是难受。。。
class Solution:
    def fairCandySwap(self, A: list, B: list):
        sum_A = sum(A)
        sum_B = sum(B)
        B_set = set(B)
        for a in A:
            if a - int((sum_A-sum_B)/2) in B_set:
                return [a,a-int((sum_A-sum_B)/2)]


if __name__ == "__main__":
    A = [2]
    B = [1,3]
    solution = Solution()
    result = solution.fairCandySwap(A,B)
    print(result)
