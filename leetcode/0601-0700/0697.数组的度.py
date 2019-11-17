#https://leetcode-cn.com/problems/degree-of-an-array/

"""
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:输入: [1, 2, 2, 3, 1];输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2:输入: [1,2,2,3,1,4,2]输出: 6
"""

class Solution:
    def findShortestSubArray(self, nums: list) -> int:
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] = dict[nums[i]] + 1
            else:
                dict[nums[i]] = 1
        sort_dict = sorted(dict.items(),key = lambda x:x[1],reverse=True)
        # print(sort_dict)
        tmp = [sort_dict[0][0]]
        for i in range(1,len(sort_dict)):
            if sort_dict[i][1] == sort_dict[0][1]:
                tmp.append(sort_dict[i][0])
            else:
                break
        ans = []
        for k in tmp:
            for j in range(len(nums)):
                if nums[j] == k:
                    left = j
                    break
            for m in range(len(nums)-1,-1,-1):
                if nums[m] == k:
                    right = m
                    break
            ans.append(right-left+1)
        return min(ans)


if __name__ == "__main__":
    nums = [1,1,2,2,2,1]
    solution = Solution()
    result = solution.findShortestSubArray(nums)
    print(result)
