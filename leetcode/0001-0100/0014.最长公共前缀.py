# https://leetcode-cn.com/problems/longest-common-prefix/

"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
"""

# ************************************#
# *************solution 1*************#
# ************************************#
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:     #如果字符串列表为空，那么就没有最长前缀
            return ""
        elif len(strs) == 1:   #如果字符串长度为1，那么他自己就是最长前缀
            return strs[0]
        elif "" in strs:
            return ""
        ###上面两种情况我也很奇怪，但是题目就是这样要求的
        else:
            num = []
            for i in range(len(strs)):
                num.append(len(strs[i]))
            m = min(num)
            ans = [[] for _ in range(m)]
            res = []
            for i in range(m):
                for j in range(len(strs)):
                    ans[i].append(strs[j][i])
                res.append(len(set(ans[i])))
            if res[0] != 1:
                return ""
            else:
                k = 0
                while k < m and res[k] == 1:
                    k = k + 1
                return strs[0][:k]

if __name__ == "__main__":
    strs = ["c","c"]
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    print(result)


# ************************************#
# *************solution 2*************#
# ************************************#
# 使用python中的zip函数
"""
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:     #如果字符串列表为空，那么就没有最长前缀
            return ""
        elif len(strs) == 1:   #如果字符串长度为1，那么他自己就是最长前缀
            return strs[0]
        ###上面两种情况我也很奇怪，但是题目就是这样要求的
        else:
            count = 0
            for w in zip(*strs):
                tmp = set(list(w))
                if len(tmp) == 1:
                    count = count + 1
                else:
                    break
            return "".join(strs[0][:count])
"""


#zip函数使用说明
# a = [1,2,3,4]
# b = [2,3,4,6]
# c = [3,4,5,6,6,7,8,9]
# for w in zip(a,b,c):
#     print(w)

