#https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例 1:输入: [3,2,1,5,6,4] 和 k = 2;输出: 5
示例 2:输入: [3,2,3,1,2,4,5,5,6] 和 k = 4;输出: 4
"""


# ************************************#
# *************solution 1*************#
# ************************************#
# 直接排序就好了，这个特别快，算法的时间复杂度是O(nlogn)
# 执行用时 :72 ms, 在所有 python3 提交中击败了99.63%的用户
# 内存消耗 :14.5 MB, 在所有 python3 提交中击败了19.51%的用户

class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]


if __name__ == "__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    solution = Solution()
    result = solution.findKthLargest(nums,k)
    print(result)