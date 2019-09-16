# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
"""


###通过逆序遍历的方式操作：逆序遍历的话删除元素不会导致元素序号的变化
###for i in range(len(nums)-1,0,-1) 也就是从len(nums)-1开始，到1，顺序是反的
# 执行用时 :152 ms, 在所有 Python3 提交中击败了34.28%的用户
# 内存消耗 :15.6 MB, 在所有 Python3 提交中击败了5.25%的用户
class Solution:
    def removeDuplicates(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                pass
        # print(nums)
        return len(nums)


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    result = solution.removeDuplicates(nums)
    print(result)
