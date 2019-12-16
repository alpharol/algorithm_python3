# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。

示例 1:输入: [3,4,5,1,2]输出: 1
示例 2:输入: [4,5,6,7,0,1,2]输出: 0
"""

# 执行用时 :40 ms, 在所有 Python 提交中击败了52.88%的用户
# 内存消耗 :12.1 MB, 在所有 Python 提交中击败了5.33%的用户
# 直接用min
"""
class Solution(object):
    def findMin(self, nums):
        return min(nums)
"""

#执行用时 :32 ms, 在所有 Python 提交中击败了91.73%的用户
#内存消耗 :12 MB, 在所有 Python 提交中击败了11.33%的用户
#遍历一次，这个算法是O(n)的
"""
class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                return nums[i + 1]
        return nums[0]
"""

#执行用时 :32 ms, 在所有 Python 提交中击败了91.73%的用户
#内存消耗 :12 MB, 在所有 Python 提交中击败了14.67%的用户
#二分查找：O(logn)
class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]
        left,right = 0,len(nums)-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == "__main__":
    nums = [5,1,2,3,4]
    solution = Solution()
    result = solution.findMin(nums)
    print(result)