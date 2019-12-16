# https://leetcode-cn.com/problems/search-insert-position/

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

输入: [1,3,5,6], 5
输出: 2

输入: [1,3,5,6], 2
输出: 1

输入: [1,3,5,6], 7
输出: 4

"""
"""
#执行用时 :72 ms, 在所有 Python3 提交中击败了24.47%的用户
#内存消耗 :13.4 MB, 在所有 Python3 提交中击败了99.85%的用户
#这个就是遍历的方法，O(n)
class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            if nums[0] > target:
                return 0
            elif nums[-1] < target:
                return len(nums)
            else:
                for i in range(len(nums)-1):
                    if nums[i] < target < nums[i+1]:
                        return i+1

"""

###二分法解题
###if中的elif个数是影响速度的，如果我加一个elif会直接超时
#执行用时 :48 ms, 在所有 Python3 提交中击败了91.30%的用户
#内存消耗 :13.7 MB, 在所有 Python3 提交中击败了51.93%的用户
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            index = (left + right) // 2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                left = index + 1
            else:
                right = index - 1
        return left


if __name__ == "__main__":
    nums = [1, 3, 6, 8,10]
    target = 6
    solution = Solution()
    result = solution.searchInsert(nums, target)
    print(result)
