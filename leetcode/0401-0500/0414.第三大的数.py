# https://leetcode-cn.com/problems/third-maximum-number/

"""
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
示例 1:输入: [3, 2, 1];输出: 1;解释: 第三大的数是 1.
示例 2:输入: [1, 2];输出: 2;解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3:输入: [2, 2, 3, 1];输出: 1;解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。
"""
###去重排序，O(nlogn)的
# 执行用时 :64 ms, 94.58%
# 内存消耗 :15 MB, 在所有 python3 提交中击败了5.26%的用户
class Solution:
    def thirdMax(self, nums: list):
        li_set = list(set(nums))
        li_set.sort()
        if len(li_set) >= 3:
            return li_set[-3]
        else:
            return li_set[-1]


if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    solution = Solution()
    result = solution.thirdMax(nums)
    print(result)
