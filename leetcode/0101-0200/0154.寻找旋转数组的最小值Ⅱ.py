# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
注意数组中可能存在重复的元素。

示例 1：输入: [1,3,5]输出: 1
示例 2：输入: [2,2,2,0,1]输出: 0
"""

# 执行用时 :48 ms, 在所有 Python 提交中击败了87.08%的用户
# 内存消耗 :12 MB, 在所有 Python 提交中击败了31.00%的用户
"""
class Solution(object):
    def findMin(self, nums):
        return min(nums)
"""

#执行用时 :48 ms, 在所有 Python 提交中击败了87.08%的用户
#内存消耗 :12 MB, 在所有 Python 提交中击败了33.00%的用户
class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        left,right = 0,len(nums)-1
        while left < right:
            mid = int((left+right)/2)
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = right - 1
        return nums[right]


if __name__ == "__main__":
    nums = [3,1,3]
    solution = Solution()
    result = solution.findMin(nums)
    print(result)