#https://leetcode-cn.com/problems/max-consecutive-ones/

"""
给定一个二进制数组， 计算其中最大连续1的个数。
示例 1:
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
"""
#872ms+14.6MB
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: list):
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        tmp = "".join(nums)
        li = tmp.split("0")
        ans = []
        for i in range(len(li)):
            ans.append(len(li[i]))
        return max(ans)
"""

#768ms+13.9MB
class Solution:
    def findMaxConsecutiveOnes(self, nums: list):
        j = 0
        tmp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                j = j + 1
            else:
                tmp = max(tmp,j)
                j = 0
        return max(tmp,j)

if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    solution = Solution()
    result = solution.findMaxConsecutiveOnes(nums)
    print(result)