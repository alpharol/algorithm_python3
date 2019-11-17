#https://leetcode-cn.com/problems/power-of-four/

"""
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
示例 1:输入: 16;输出: true
示例 2:输入: 5;输出: false
"""

class Solution:
    def isPowerOfFour(self, num):
        if num == 0:
            return False
        elif num == 1:
            return True
        elif num == 2 or num == 3:
            return False
        else:
            while num / 4 != 1:
                if num % 4 != 0:
                    return False
                else:
                    num = num / 4
            return True


if __name__ == "__main__":
    num = 5
    solution = Solution()
    result = solution.isPowerOfFour(num)
    print(result)