# https://leetcode-cn.com/problems/maximum-subarray/

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""

# 执行用时 :80 ms, 在所有 python3 提交中击败了88.55%的用户
# 内存消耗 :13.5 MB, 在所有 python3 提交中击败了86.16%的用户
# 运用了动态规划的思想，后一个数的最大子序和和前一个数是完全相关的。
class Solution:
    def maxSubArray(self, nums):
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if ans[i-1] < 0:
                ans.append(nums[i])
            else:
                ans.append(ans[i-1]+nums[i])
        return max(ans)

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    result = solution.maxSubArray(nums)
    print(result)
