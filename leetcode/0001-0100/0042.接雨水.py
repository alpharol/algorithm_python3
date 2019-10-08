#https://leetcode-cn.com/problems/trapping-rain-water/

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
图片可以去看链接
示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""

class Solution:
    def trap(self, height):
        if len(height) == 0:
            return 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        for i in range(1,len(height)):
            max_left[i] = max(height[i],max_left[i-1])
        for i in range(len(height)-2,-1,-1):
            max_right[i] = max(height[i],max_right[i+1])
        res = 0
        for i in range(len(height)):
            res = res + min(max_left[i],max_right[i])-height[i]
        return res

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    result = solution.trap(height)
    print(result)
