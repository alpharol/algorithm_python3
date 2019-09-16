# https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""


# 26ms+5860k
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            ans = [0, 1]
            k = n - 1
            while k > 0:
                ans.append(ans[-1] + ans[-2])
                k = k - 1
            return ans[-1]

if __name__ == "__main__":
    n = 3
    solution = Solution()
    result = solution.Fibonacci(n)
    print(result)
