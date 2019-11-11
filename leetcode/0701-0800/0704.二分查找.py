#https://leetcode-cn.com/problems/binary-search/

"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:输入: nums = [-1,0,3,5,9,12], target = 9;输出: 4;解释: 9 出现在 nums 中并且下标为 4

示例 2:输入: nums = [-1,0,3,5,9,12], target = 2;输出: -1;解释: 2 不存在 nums 中因此返回 -1
"""

class Solution:
    def search(self, nums: list, target):
        l,r = 0,len(nums)-1
        while l <= r:
            m = int((l+r)/2)
            if nums[m] < target:
                l = m+1    #####这个+1很重要，要不然就死循环
            elif nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1    #####这个-1很重要，要不然就死循环
        return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 2
    solution = Solution()
    result = solution.search(nums,target)
    print(result)
