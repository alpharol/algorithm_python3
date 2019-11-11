#https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/

"""
在一个给定的数组nums中，总是存在一个最大元素 。
查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
如果是，则返回最大元素的索引，否则返回-1。

示例 1:输入: nums = [3, 6, 1, 0];输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
 
示例 2:输入: nums = [1, 2, 3, 4];输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.
"""

# ************************************#
# *************solution 1*************#
# ************************************#
# 执行用时 :52 ms, 在所有 python3 提交中击败了70.76%的用户
# 内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.53%的用户
"""
class Solution:
    def dominantIndex(self, nums: list):
        tmp_max = max(nums)
        #print(tmp_max)
        index_max = nums.index(tmp_max)
        nums.pop(index_max)
        #print(nums)
        for w in nums:
            #print(w)
            if w*2 <= tmp_max:
                pass
            else:
                return -1
        return index_max
"""



# ************************************#
# *************solution 2*************#
# ************************************#
# 执行用时 :44 ms, 在所有 python3 提交中击败了93.93%的用户
# 内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.53%的用户
class Solution:
    def dominantIndex(self, nums: list):
        if len(nums) <= 1:
            return 0
        else:
            tmp_max = max(nums)
            index_max = nums.index(tmp_max)
            sorted_num = sorted(nums)
            if sorted_num[-2]*2 <= sorted_num[-1]:
                return index_max
            else:
                return -1



if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    result = solution.dominantIndex(nums)
    print(result)