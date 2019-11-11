#https://leetcode-cn.com/problems/min-cost-climbing-stairs/

"""
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:输入: cost = [10, 15, 20];输出: 15;解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

示例 2:输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1];输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
"""

#执行用时 :48 ms, 在所有 Python 提交中击败了97.30%的用户
#内存消耗 :11.9 MB, 在所有 Python 提交中击败了14.36%的用户
class Solution(object):
    def minCostClimbingStairs(self, cost):
        ans = [cost[0],cost[1]]
        k = 2
        while k <= len(cost)-1:
            tmp = min((ans[-1]+cost[k]),(ans[-2]+cost[k]))
            ans.append(tmp)
            k = k + 1
        return min(ans[-1],ans[-2])

if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    solution = Solution()
    result = solution.minCostClimbingStairs(cost)
    print(result)