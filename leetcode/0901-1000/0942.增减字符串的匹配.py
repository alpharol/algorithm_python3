#https://leetcode-cn.com/problems/di-string-match/

"""
给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]
 
示例 1：输出："IDID";输出：[0,4,1,3,2]
示例 2：输出："III";输出：[0,1,2,3]
示例 3：输出："DDI";输出：[3,2,0,1]
"""
###这个方法没有问题，但是超出了时间限制
"""
class Solution:
    def diStringMatch(self, S):
        tmp = [i for i in range(len(S)+1)]
        #tmp = num[:]
        ans = []
        for s in S:
            if s == "I":
                ans.append(min(tmp))
                tmp.pop(0)
            else:
                ans.append(max(tmp))
                tmp.pop(-1)
        return ans+tmp
"""



#执行用时 :92 ms, 在所有 Python3 提交中击败了98.94%的用户
#内存消耗 :15.1 MB, 在所有 Python3 提交中击败了5.60%的用户
##可以不用列表的运作，尽量不要做列表的操作，慢！！！
class Solution:
    def diStringMatch(self, S):
        low,high = 0,len(S)
        ans = []
        for s in S:
            if s == "I":
                ans.append(low)
                low = low + 1
            else:
                ans.append(high)
                high = high - 1
        ans.append(int((low+high)/2))
        return ans


if __name__ == "__main__":
    S = "DDI"
    solution = Solution()
    result = solution.diStringMatch(S)
    print(result)