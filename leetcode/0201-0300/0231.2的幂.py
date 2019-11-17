#https://leetcode-cn.com/problems/power-of-two/

"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:输入: 1;输出: true
示例 2:输入: 16;输出: true
示例 3:输入: 218;输出: false
"""


#执行用时 :48 ms, 在所有 Python3 提交中击败了87.90%的用户
#内存消耗 :14 MB, 在所有 Python3 提交中击败了5.98%的用户

class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        else:
            i = 1
            while i <= n:
                if int(n / i) != n / i:
                    return  False
                else:
                    pass
                i = i * 2
            return True

if __name__ == "__main__":
    n = 256
    solution = Solution()
    result = solution.isPowerOfTwo(n)
    print(result)