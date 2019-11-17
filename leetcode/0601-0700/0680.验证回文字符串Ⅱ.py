#https://leetcode-cn.com/problems/valid-palindrome-ii/

"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:输入: "aba";输出: True
示例 2:输入: "abca";输出: True;解释: 你可以删除c字符。
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            l,r = 0,len(s)-1
            while l <= r:
                if s[l] == s[r]:
                    l = l + 1
                    r = r - 1
                else:
                    tmp_1 = s[:l]+s[l+1:]
                    tmp_2 = s[:r]+s[r+1:]
                    return tmp_1==tmp_1[::-1] or tmp_2==tmp_2[::-1]


if __name__ == "__main__":
    s = "abdca"
    solution = Solution()
    result = solution.validPalindrome(s)
    print(result)