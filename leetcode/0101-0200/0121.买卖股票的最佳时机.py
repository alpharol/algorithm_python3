#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

示例 1:输入: [7,1,5,3,6,4];输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:输入: [7,6,4,3,1];输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

# ************************************#
# *************solution 2*************#
# ************************************#
#在优化之后，可以把时间复杂度降低为O(n)
#执行用时 :76 ms, 在所有 Python3 提交中击败了97.42%的用户
#内存消耗 :14.9 MB, 在所有 Python3 提交中击败了5.32%的用户
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        tmp = prices[0]
        num = []
        for i in range(len(prices)):
            if prices[i] < tmp:
                tmp = prices[i]
            elif prices[i] > tmp:
                num.append(prices[i]-tmp)
        if len(num) == 0:
            return 0
        else:
            return max(num)

if __name__ == "__main__":
    nums = [7,1,5,3,6,4]
    solution = Solution()
    result = solution.maxProfit(nums)
    print(result)


# ************************************#
# *************solution 1*************#
# ************************************#
#O(n^2)的算法，超出了时间复杂度
"""
class Solution:
    def maxProfit(self, prices) -> int:
        num = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                tmp = prices[j] - prices[i]
                if tmp >= 0:
                    num.append(tmp)
        if len(num) != 0:
            return max(num)
        else:
            return 0
"""