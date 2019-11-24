#https://leetcode-cn.com/problems/contains-duplicate-ii/

"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:输入: nums = [1,2,3,1], k = 3;输出: true
示例 2:输入: nums = [1,0,1,1], k = 1;输出: true
示例 3:输入: nums = [1,2,3,1,2,3], k = 2;输出: false
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = int(i)
            elif i - dict[nums[i]] > k:
                dict[nums[i]] = int(i)
            else:
                return True
        return False

if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    k = 2
    solution = Solution()
    result = solution.containsNearbyDuplicate(nums,k)
    print(result)
