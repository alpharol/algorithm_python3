#https://leetcode-cn.com/problems/climbing-stairs/

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：输入： 2;输出： 2;
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：输入： 3;输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""

#执行用时 :76 ms, 在所有 Python3 提交中击败了8.78%的用户
#内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.14%的用户
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1,2]
        k = n - 2
        while k > 0:
            ans.append(ans[-1]+ans[-2])
            k = k - 1
        return ans[-1]

if __name__ == "__main__":
    n = 4
    solution = Solution()
    result = solution.climbStairs(n)
    print(result)