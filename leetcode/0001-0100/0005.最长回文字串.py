# https://leetcode-cn.com/problems/longest-palindromic-substring/

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：输入: "babad";输出: "bab"
注意: "aba" 也是一个有效答案

示例 2：输入: "cbbd";输出: "bb"
"""

# ************************************#
# *************solution 1*************#
# ************************************#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        elif len(s) == 1:
            return s
        else:
            dp = [[0] * len(s) for _ in range(len(s))]
            max_len = 1
            anx = s[0]
            for i in range(len(s)):
                for j in range(i + 1):
                    if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1] == 1):
                        dp[i][j] = 1
                    # 如果已经验证是回文串了同时长度也是最长的，那么就直接更改res就好了
                    if dp[i][j] == 1 and max_len <= i - j + 1:
                        ans = s[j:i + 1]
                        max_len = i - j + 1
            return ans


if __name__ == "__main__":
    s = "aba"
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(result)




# ************************************#
# *************solution 2*************#
# ************************************#
#####暴力解题法：遍历所有的可能的字符串然后判断其是否是回文串，注意这个时间复杂度是O(n^3)，因为后面还需要验证回文串
#####超出了时间限制
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        elif len(s) == 1:
            return s
        else:
            num = []
            stri = []
            for i in range(len(s)-1):
                for j in range(i+1,len(s)+1):
                    tmp = s[i:j]
                    if tmp == tmp[::-1]:
                        num.append(len(tmp))
                        stri.append(tmp)
            max_len = max(num)
            return stri[num.index(max_len)]
"""