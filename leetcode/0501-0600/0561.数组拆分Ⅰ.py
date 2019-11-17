#https://leetcode-cn.com/problems/array-partition-i/

"""
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，
使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:输入: [1,4,3,2];输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
"""

class Solution:
    def arrayPairSum(self, nums: list):
        nums.sort()
        tmp = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                tmp = tmp + nums[i]
        return tmp


if __name__ == "__main__":
    nums = [1,4,3,2]
    solution = Solution()
    result = solution.arrayPairSum(nums)
    print(result)
