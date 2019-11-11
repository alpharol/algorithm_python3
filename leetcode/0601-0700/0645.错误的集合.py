#https://leetcode-cn.com/problems/set-mismatch/submissions/

"""
集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，
导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:输入: nums = [1,2,2,4];输出: [2,3]
"""

class Solution:
    def findErrorNums(self, nums: list):
        ans = [0,0]
        ans[0] = sum(nums)-sum(list(set(nums)))   #重复的数字
        ans[1] = int((1+len(nums))*len(nums)/2-sum(list(set(nums))))
        return ans

if __name__ == "__main__":
    nums = [1,5,3,2,2,7,6,4,8,9]
    solution = Solution()
    result = solution.findErrorNums(nums)
    print(result)