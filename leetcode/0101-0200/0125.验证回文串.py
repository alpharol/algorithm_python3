# https://leetcode-cn.com/problems/valid-palindrome/

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""


# 这是一个O(n)的方法，需要额外的空间
# 执行用时 :96 ms, 在所有 Python3 提交中击败了27.13%的用户
# 内存消耗 :14.4 MB, 在所有 Python3 提交中击败了27.26%的用户
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            tmp = ""
            alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                     "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3",
                     "4", "5", "6", "7", "8", "9"]
            for k in s:
                if k in alpha:
                    tmp = tmp + k
            tmp = tmp.lower()
            # print(tmp)
            if tmp == tmp[::-1]:
                return True
            else:
                return False


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)



