# https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode/

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:输入: [2,2,1];输出: 1
示例 2:输入: [4,1,2,1,2];输出: 4
"""

# ************************************#
# *************solution 3*************#
# ************************************#
###使用哈希表
#执行用时 :204 ms, 在所有 Python3 提交中击败了8.46%的用户
#内存消耗 :16.2 MB, 在所有 Python3 提交中击败了5.03%的用户
class Solution(object):
    def singleNumber(self, nums):
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table.pop(i)
            else:
                hash_table[i] = 1
        return hash_table.popitem()[0]   ###popitem表示随机返回并删除字典中的一对键值


if __name__ == "__main__":
    nums = [2,2,1]
    solution = Solution()
    result = solution.singleNumber(nums)
    print(result)


# ************************************#
# *************solution 1*************#
# ************************************#
###使用列表的方法
# 执行用时 :1864 ms, 在所有 Python3 提交中击败了5.00%的用户，时间复杂度O(n^2)
# 内存消耗 :16.3 MB, 在所有 Python3 提交中击败了5.03%的用户，空间复杂度O(n)
"""
class Solution:
    def singleNumber(self, nums):
        ans = []
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
            else:
                ans.remove(nums[i])
        return ans[0]
"""


# ************************************#
# *************solution 2*************#
# ************************************#
###使用数学方法
#执行用时 :248 ms, 在所有 Python3 提交中击败了8.43%的用户
#内存消耗 :16.3 MB, 在所有 Python3 提交中击败了5.03%的用户
"""
class Solution:
    def singleNumber(self, nums):
        num_set = list(set(nums))
        s = sum(num_set)
        return 2*s - sum(nums)
"""