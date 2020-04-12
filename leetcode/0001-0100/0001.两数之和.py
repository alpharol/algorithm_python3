# https://leetcode-cn.com/problems/two-sum/

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

# ************************************#
# *************solution 3*************#
# ************************************#
# 使用哈希数据结构，这样的算法时间复杂度就会很低，查找只需要O(1)的时间，其实整体上就是O(n)的方法了。
#执行用时 :92 ms, 在所有 Python3 提交中击败了52.67%的用户
#内存消耗 :15 MB, 在所有 Python3 提交中击败了5.05%的用户
class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        ans = []
        for i in range(len(nums)):
            other = target - nums[i]
            if other in lookup:
                ans.append(lookup[other])
                ans.append(i)
                break
            else:
                lookup[nums[i]] = i
        return ans


if __name__ == "__main__":
    nums = [3, 4, 2, 4, 5, 9]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)




# ************************************#
# *************solution 1*************#
# ************************************#
# 循环嵌套，暴力解法，时间复杂度高，不通过，时间复杂度是O(n^2)
"""
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
"""



# ************************************#
# *************solution 2*************#
# ************************************#
# 使用index查找，这样可以只需要一个循环，比较快，但是in函数在查找列表的时候，速度其实是非常慢的，也可以说成是O(n^2)的方法
#执行用时 :1764 ms, 在所有 Python3 提交中击败了22.33%的用户
#内存消耗 :14.8 MB, 在所有 Python3 提交中击败了6.40%的用户
"""
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            ans = [i]
            other = target - nums[i]
            if other in nums[i + 1:]:
                k = nums[i + 1:].index(other)+i+1
                ans.append(k)
                break
        return ans
"""