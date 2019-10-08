# https://leetcode-cn.com/problems/palindrome-number/

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""

# ************************************#
# *************solution 2*************#
# ************************************#
#执行用时 :120 ms, 在所有 Python3 提交中击败了32.55%的用户
#内存消耗 :14.2 MB, 在所有 Python3 提交中击败了5.01%的用户
###题目中强调不用字符串
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            y = x
            res = 0
            while y > 0:
                res = res * 10 + y % 10
                y = int(y / 10)
            return res == x

if __name__ == "__main__":
    x = 321
    solution = Solution()
    result = solution.isPalindrome(x)
    print(result)


# ************************************#
# *************solution 1*************#
# ************************************#
###使用字符串的方法，速度是非常快的
#执行用时 :72 ms, 在所有 Python3 提交中击败了98.51%的用户
#内存消耗 :14.1 MB, 在所有 Python3 提交中击败了5.01%的用户
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
"""