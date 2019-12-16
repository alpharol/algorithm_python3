# https://leetcode-cn.com/problems/sqrtx/

"""
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:输入: 4,输出: 2
示例 2:输入: 8,输出: 2,说明: 8 的平方根是 2.82842...,由于返回类型是整数,小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            a, b = 1, x  ###sqrt(x) <= (a+1)/2
            while a < b:
                m = (a + b) // 2
                if m ** 2 <= x < (m + 1) ** 2:
                    return m
                elif x >= (m+1)**2:
                    a = m
                else:
                    b = m


if __name__ == "__main__":
    x = 0
    solution = Solution()
    result = solution.mySqrt(x)
    print(result)
