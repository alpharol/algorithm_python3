#https://leetcode-cn.com/problems/minimum-size-subarray-sum/

"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
如果不存在符合条件的连续子数组，返回 0。

示例: 输入: s = 7, nums = [2,3,1,2,4,3];输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        i,j = 0,0
        tmp = 0
        ans = []
        while i < len(nums):
            if j < len(nums) and tmp < s:
                tmp = tmp + nums[j]
                j = j + 1
            else:
                tmp = tmp - nums[i]
                i  = i + 1
            if tmp >= s:
                ans.append(j-i)
        if len(ans) > 0:
            return min(ans)
        else:
            return 0


if __name__ == "__main__":
    s = 7
    nums = [8,3,1,2,4,3]
    solution = Solution()
    result = solution.minSubArrayLen(s,nums)
    print(result)




