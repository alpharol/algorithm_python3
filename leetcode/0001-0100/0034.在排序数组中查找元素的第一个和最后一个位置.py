# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:输入: nums = [5,7,7,8,8,10], target = 8;输出: [3,4]
示例 2:输入: nums = [5,7,7,8,8,10], target = 6;输出: [-1,-1]
"""

# 遍历数组，这是一个O(n)的算法，题目中要求算法的时间复杂度为O(nlogn)，所以是需要使用二分查找的。
# 执行用时 :84 ms, 在所有 Python 提交中击败了98.40%的用户
# 内存消耗 :13.4 MB, 在所有 Python 提交中击败了5.32%的用户
"""
class Solution(object):
    def searchRange(self, nums, target):
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        if res == []:
            return [-1,-1]
        elif len(res) == 1:
            return [res[0],res[0]]
        else:
            return [min(res),max(res)]
"""

#执行用时 :92 ms, 在所有 Python 提交中击败了86.62%的用户
#内存消耗 :12.9 MB, 在所有 Python 提交中击败了40.19%的用户
#使用二分查找的方法
class Solution(object):
    def searchRange(self, nums, target):
        if nums == []:
            return [-1,-1]
        l_1, r_1 = 0, len(nums)
        while l_1 < r_1:
            mid_1 = int((l_1 + r_1) / 2)
            if nums[mid_1] == target:
                r_1 = mid_1    ###区间是左闭右开的，所以right不用加减，但是left需要加1
            elif nums[mid_1] < target:
                l_1 = mid_1 + 1
            elif nums[mid_1] > target:
                r_1 = mid_1
        if l_1 == len(nums):
            a = -1
        elif nums[l_1] == target:
            a = l_1
        else:
            a = -1

        l_2, r_2 = 0, len(nums)
        while l_2 < r_2:
            mid_2 = int((l_2+r_2)/2)
            if nums[mid_2] == target:
                l_2 = mid_2 + 1
            elif nums[mid_2] < target:
                l_2 = mid_2 + 1
            elif nums[mid_2] > target:
                r_2 = mid_2
        if l_2 == 0:
            b = -1
        elif nums[l_2-1] == target:
            b = l_2-1
        else:
            b = -1
        return [a,b]



if __name__ == "__main__":
    nums = [1]
    target = 1
    solution = Solution()
    result = solution.searchRange(nums, target)
    print(result)
