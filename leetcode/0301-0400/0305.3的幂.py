#https://leetcode-cn.com/problems/power-of-three/

"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。
示例 1:输入: 27;输出: true
示例 2:输入: 0;输出: false
示例 3:输入: 9;输出: true
示例 4:输入: 45;输出: false
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            while n / 3 != 1:
                if n % 3 != 0:
                    return False
                else:
                    n = n / 3
            return True

if __name__ == "__main__":
    n = 1
    solution = Solution()
    result = solution.isPowerOfThree(n)
    print(result)