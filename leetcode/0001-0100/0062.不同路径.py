#https://leetcode-cn.com/problems/unique-paths/submissions/

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28
"""

####使用阶乘的数学方法做
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        jiecheng_1, jiecheng_2, jiecheng_3 = 1, 1, 1
        for i in range(m + n - 2):
            jiecheng_1 = jiecheng_1 * (i + 1)
        for j in range(m - 1):
            jiecheng_2 = jiecheng_2 * (j + 1)
        for m in range(n - 1):
            jiecheng_3 = jiecheng_3 * (m + 1)
        return jiecheng_1 / jiecheng_2 / jiecheng_3
"""

class Solution:
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                #等于上边和左边的值相加
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == "__main__":
    m = 7
    n = 3
    solution = Solution()
    result = solution.uniquePaths(m, n)
    print(int(result))