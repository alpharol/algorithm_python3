#https://leetcode-cn.com/problems/valid-perfect-square/solution/xun-huan-mi-yun-suan-by-loulan/

"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
说明：不要使用任何内置的库函数，如  sqrt。

示例 1：输入：16;输出：True
示例 2：输入：14;输出：False
"""

class Solution:
    def isPerfectSquare(self, num: int):
        l,r = 0,num
        if num == 0 or num == 1:
            return True
        while l < r:
            mid = (l+r)//2
            tmp = mid*mid
            if tmp < num:
                l = mid+1
            elif tmp == num:
                return True
            else:
                r = mid
        return False

if __name__ == "__main__":
    num = 1
    solution = Solution()
    result = solution.isPerfectSquare(num)
    print(result)