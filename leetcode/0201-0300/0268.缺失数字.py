#https://leetcode-cn.com/problems/missing-number/submissions/

"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
示例 1:输入: [3,0,1]输出: 2
示例 2:输入: [9,6,4,2,3,5,7,0,1]输出: 8
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        for i in range(len(nums)+1):
            tmp = tmp + i
        return tmp - sum(nums)

if __name__ == "__main__":
    nums = [3,0,1]
    solution = Solution()
    result = solution.missingNumber(nums)
    print(result)