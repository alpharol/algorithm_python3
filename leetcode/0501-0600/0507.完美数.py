#https://leetcode-cn.com/problems/perfect-number/

"""
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False

示例：输入: 28;输出: True;解释: 28 = 1 + 2 + 4 + 7 + 14
"""

# ************************************#
# *************solution 1*************#
# ************************************#
"""
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        ans = []
        for i in range(int(math.sqrt(num))):
            if num % (i+1) == 0:
                ans.append(i+1)
                ans.append(int(num / (i+1)))
        ans.remove(num)
        return sum(ans) == num
"""

# ************************************#
# *************solution 2*************#
# ************************************#
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        ans = []
        i = 1
        while (i*i <= num):
            if num % i == 0:
                ans.append(i)
                ans.append(int(num/i))
            i = i + 1
        ans.remove(num)
		# 防止这个数字是一个完全平方数
        if (i-1)**2 == num:
            ans.remove(i-1)
        return sum(ans) == num

if __name__ == "__main__":
    n = 28
    solution = Solution()
    result = solution.checkPerfectNumber(num=n)
    print(result)

