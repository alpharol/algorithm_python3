#https://leetcode-cn.com/problems/majority-element/

"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:输入: [3,2,3];输出: 3
示例 2:输入: [2,2,1,1,1,2,2];输出: 2
"""

#******************************************************#
#******************Solution 2:哈希表******************#
#******************************************************#
#执行用时 :288 ms, 在所有 Python3 提交中击败了5.49%的用户
#内存消耗 :15.3 MB, 在所有 Python3 提交中击败了5.48%的用户
####众数要求出现次数大于n/2，所以排序之后的中位数一定是众数
class Solution:
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]

        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict.keys():
                #print(nums[i])
                dict[nums[i]] = 1
            else:
                tmp = nums[i]
                dict[nums[i]] = dict[nums[i]] + 1
                if dict[nums[i]] > len(nums)/2:
                    break
        return tmp


if __name__ == "__main__":
    nums = [6,5,5]
    solution = Solution()
    result = solution.majorityElement(nums)
    print(result)


#******************************************************#
#******************Solution 1:数学方法******************#
#******************************************************#
#执行用时 :240 ms, 在所有 Python3 提交中击败了5.49%的用户
#内存消耗 :15.2 MB, 在所有 Python3 提交中击败了5.48%的用户
####众数要求出现次数大于n/2，所以排序之后的中位数一定是众数
###这个算法的时间复杂度是O(nlogn)
"""
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[(len(nums)+1)//2-1]
"""