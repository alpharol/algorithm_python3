#https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/

"""
给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。
这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.

示例 1:输入: [3, 1, 4, 1, 5], k = 2;输出: 2
解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。

示例 2:输入:[1, 2, 3, 4, 5], k = 1;输出: 4
解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。

示例 3:输入: [1, 3, 1, 5, 4], k = 0;输出: 1
解释: 数组中只有一个 0-diff 数对，(1, 1)。
"""


class Solution:
    def findPairs(self, nums: list, k: int):
        dict = {}
        re = 0
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            elif dict[nums[i]] == 1:
                re = re + 1
                dict[nums[i]] = 2
            else:
                pass
        if k < 0:
            return 0
        elif k == 0:
            return re
        else:
            count = 0
            for i in range(len(dict)):
                if list(dict.keys())[i] + k in list(dict.keys()):
                    count = count + 1
            return count


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 1
    solution = Solution()
    result = solution.findPairs(nums,k)
    print(result)


