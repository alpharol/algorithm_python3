#https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/

"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。

示例 1:输入: [2, 6, 4, 8, 10, 9, 15];输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
"""

class Solution:
    def findUnsortedSubarray(self, nums: list) -> int:
        right_nums = sorted(nums)
        if nums == right_nums:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] != right_nums[i]:
                    left = i
                    break
            for j in range(len(nums)-1,-1,-1):
                if nums[j] != right_nums[j]:
                    right = j
                    break
            return right+1-left

if __name__ == "__main__":
    nums = [2, 6, 4, 8, 10, 9, 15]
    solution = Solution()
    result = solution.findUnsortedSubarray(nums)
    print(result)