#https://leetcode-cn.com/problems/intersection-of-two-arrays/

"""
给定两个数组，编写一个函数来计算它们的交集。
示例 1:输入: nums1 = [1,2,2,1], nums2 = [2,2];输出: [2]
示例 2:输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4];输出: [9,4]
"""

# ************************************#
# *************solution 2*************#
# ************************************#
###使用哈希表是最快的
#执行用时 :68 ms, 在所有 Python3 提交中击败了72.75%的用户
#内存消耗 :14 MB, 在所有 Python3 提交中击败了5.02%的用户
class Solution:
    def intersection(self, nums1: list, nums2: list):
        nums1_list = list(set(nums1))
        nums2_list = list(set(nums2))
        num = nums1_list + nums2_list
        dic = {}
        ans = []
        for x in num:
            if x in dic:
                ans.append(x)
            else:
                dic[x] = 1
        return ans


if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    solution = Solution()
    result = solution.intersection(nums1,nums2)
    print(result)



# ************************************#
# *************solution 1*************#
# ************************************#
#执行用时 :88 ms, 在所有 Python3 提交中击败了38.83%的用户
#内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.02%的用户
"""
class Solution:
    def intersection(self, nums1: list, nums2: list):
        nums1_list = list(set(nums1))
        nums2_list = list(set(nums2))
        ans = []
        for i in range(len(nums1_list)):
            if nums1_list[i] in nums2_list:
                ans.append(nums1_list[i])
        return ans
"""