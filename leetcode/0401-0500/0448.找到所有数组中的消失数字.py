# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/

"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:输入:[4,3,2,7,8,2,3,1];输出:[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums: list):
        ans = []
        #nums_li = list(set(nums))
        n = 1
        while n <= len(nums):
           if n not in nums:
               ans.append(n)
           else:
               pass
           n = n + 1
        return ans

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    solution = Solution()
    result = solution.findDisappearedNumbers(nums)
    print(result)




num = [2,5,4,9,10,6,7,8,11]

print(max_num(num))
