# https://leetcode-cn.com/problems/is-subsequence/

"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:s = "abc", t = "ahbgdc" 返回 true.

示例 2:s = "axc", t = "ahbgdc" 返回 false.
"""

#满足无后效性，只需要考虑当前的情况
#满足从局部最优到全局最优
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i < len(s):
            tmp_s = s[i]
            while j < len(t):
                tmp_t = t[j]
                if tmp_s == tmp_t:
                    i = i + 1
                    j = j + 1
                    break
                else:
                    j = j + 1
            if j == len(t) and i < len(s):
                return False

        return len(s) == i

if __name__ == "__main__":
    s = "axc"
    t = "ahbgdc"
    solution = Solution()
    result = solution.isSubsequence(s,t)
    print(result)



