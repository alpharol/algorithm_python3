#https://leetcode-cn.com/problems/add-digits/

"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:输入: 38;输出: 2
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
"""

class Solution(object):
    def addDigits(self, num):
        while len(str(num)) > 1:
            tmp = 0
            for w in str(num):
                tmp = tmp + int(w)
            num = tmp
        return num

if __name__ == "__main__":
    num = 38
    solution = Solution()
    result = solution.addDigits(num)
    print(result)
