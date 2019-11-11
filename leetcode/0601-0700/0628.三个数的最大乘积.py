#https://leetcode-cn.com/problems/maximum-product-of-three-numbers/

"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:输入: [1,2,3];输出: 6
示例 2:输入: [1,2,3,4];输出: 24
"""

class Solution:
    def maximumProduct(self, nums: list) -> int:
        nums.sort()
        tmp_1 = nums[-1]*nums[-2]*nums[-3]
        tmp_2 = nums[0]*nums[1]*nums[-1]
        if tmp_1 < tmp_2:
            return tmp_2
        else:
            return tmp_1

if __name__ == "__main__":
    nums = [1,2,3,4]
    solution = Solution()
    result = solution.maximumProduct(nums)
    print(result)