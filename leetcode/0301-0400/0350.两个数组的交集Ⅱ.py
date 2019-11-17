#https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/

"""
给定两个数组，编写一个函数来计算它们的交集。
示例 1:输入: nums1 = [1,2,2,1], nums2 = [2,2];输出: [2,2]
示例 2:输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4];输出: [4,9]
说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
"""

class Solution:
    def intersect(self, nums1: list, nums2: list):
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums1[i])
                nums2.remove(nums1[i])
        return ans


if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2]
    solution = Solution()
    result = solution.intersect(nums1, nums2)
    print(result)