# https://leetcode-cn.com/problems/powx-n/

"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
示例 1:输入: 2.00000, 10;输出: 1024.00000
示例 2:输入: 2.10000, 3;输出: 9.26100
示例 3:输入: 2.00000, -2;输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
"""
####使用递归算法，时间复杂度是O(logn)
class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1/self.helper(x,-n)
        else:
            return self.helper(x,n)

    def helper(self,x,n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            return self.helper(x*x,n/2)
        else:
            return self.helper(x*x,(n-1)/2)*x


if __name__ == "__main__":
    x = 2.00000
    n = 10
    solution = Solution()
    result = solution.myPow(x,n)
    print(result)


###这样的遍历超出了时间的限制，这可以说是一个O(n)的算法
"""
class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            m = -n
            if m == 1:
                return 1 / x
            else:
                tmp = 1
                while m > 0:
                    tmp = tmp * x
                    m = m - 1
                return 1 / tmp
        elif n == 0:
            return 1
        else:
            if n == 1:
                return x
            else:
                tmp = 1
                while n > 0:
                    tmp = tmp * x
                    n = n - 1
                return tmp
"""
