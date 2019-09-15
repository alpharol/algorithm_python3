#https://leetcode-cn.com/problems/contains-duplicate/

"""
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:输入: [1,2,3,1];输出: true
示例 2:输入: [1,2,3,4];输出: false
示例 3:输入: [1,1,1,3,3,4,3,2,4,2];输出: true
"""

#使用哈希表方法
#执行用时 :180 ms, 在所有 Python3 提交中击败了59.34%的用户
#内存消耗 :20 MB, 在所有 Python3 提交中击败了6.58%的用户
class Solution:
    def containsDuplicate(self, nums):
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return True
            else:
                dict[nums[i]] = 1
        return False

if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2]
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)