#https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:nums1 = [1, 3] nums2 = [2] 则中位数是 2.0
示例 2:nums1 = [1, 2] nums2 = [3, 4] 则中位数是 (2 + 3)/2 = 2.5
"""

# ************************************#
# *************solution 1*************#
# ************************************#
####方法一：直接对两个数组排序，我没想到这也可以的。。。。
#执行用时 :68 ms, 在所有 Python3 提交中击败了96.47%的用户
#内存消耗 :13.2 MB, 在所有 Python3 提交中击败了95.34%的用户
#算法的时间复杂度是O((m+n)log(m+n))
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 == 0:
            return float((nums[int(len(nums)/2-1)]+nums[int(len(nums)/2)])/2)
        else:
            return float(nums[int((len(nums)-1)/2)])
"""


# ************************************#
# *************solution 2*************#
# ************************************#
#执行用时 :96 ms, 在所有 Python3 提交中击败了33.40%的用户
#内存消耗 :13.2 MB, 在所有 Python3 提交中击败了94.87%的用户
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        index1,index2 = 0,0
        tmp = []
        while index1 <= len(nums1)-1 and index2 <= len(nums2)-1:
            if nums1[index1] <= nums2[index2]:
                tmp.append(nums1[index1])
                index1 = index1 + 1
            else:
                tmp.append(nums2[index2])
                index2 = index2 + 1
        tmp = tmp + nums1[index1:]+nums2[index2:]
        if len(tmp) % 2 != 0:
            return float(tmp[int((len(tmp)-1)/2)])
        else:
            return float((tmp[int(len(tmp)/2)]+tmp[int(len(tmp)/2-1)])/2)

if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    solution = Solution()
    result = solution.findMedianSortedArrays(nums1,nums2)
    print(result)