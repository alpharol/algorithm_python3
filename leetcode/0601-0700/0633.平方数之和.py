#https://leetcode-cn.com/problems/sum-of-square-numbers/


"""
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
示例1:输入: 5;输出: True;解释: 1 * 1 + 2 * 2 = 5
示例2:输入: 3;输出: False
"""
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j = int(math.sqrt(c))
        i = 0
        while i <= j:
            if i**2+j**2 == c:
                return True
            elif i**2+j**2 > c:
                j = j - 1
            else:
                i = i + 1
        return False


if __name__ == "__main__":
    c= 102
    solution = Solution()
    result = solution.judgeSquareSum(c)
    print(result)
