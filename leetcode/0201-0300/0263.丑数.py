#https://leetcode-cn.com/problems/ugly-number/

"""
编写一个程序判断给定的数是否为丑数。
丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:输入: 6;输出: true;解释: 6 = 2 × 3
示例 2:输入: 8;输出: true;解释: 8 = 2 × 2 × 2
示例 3:输入: 14;输出: false ;解释: 14 不是丑数，因为它包含了另外一个质因数 7。
"""

class Solution(object):
    def isUgly(self, num):
        if num == 0:
            return False
        elif num == 1:
            return True
        else:
            while num != 1:
                if num % 2 == 0:
                    num = num / 2
                elif num % 3 == 0:
                    num = num / 3
                elif num % 5 == 0:
                    num = num / 5
                else:
                    return False
            return True

if __name__ == "__main__":
    num = 14
    solution = Solution()
    result = solution.isUgly(num)
    print(result)