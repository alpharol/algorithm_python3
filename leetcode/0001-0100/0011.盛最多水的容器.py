# https://leetcode-cn.com/problems/container-with-most-water/

"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""

# ************************************#
# *************solution 1*************#
# ************************************#
###O(n^2)的算法时间超时了，方法应该是可以的
"""
class Solution:
    def maxArea(self, height):
        n = len(height)
        maxarea = []
        for i in range(n):
            for j in range(i+1, n):
                    maxarea.append(min(height[i],height[j])*(j-i))
        return max(maxarea)
"""

# ************************************#
# *************solution 2*************#
# ************************************#
# 这个方法比较好，双指针只需要遍历一遍就好了，时间复杂度只有O(n)
# 执行用时 :116 ms, 在所有 Python3 提交中击败了96.12%的用户
# 内存消耗 :14.7 MB, 在所有 Python3 提交中击败了32.55%的用户
class Solution:
    def maxArea(self, height):
        n = len(height)
        res = min(height[0],height[n-1])*(n-1)
        i = 0
        j = n - 1
        while i != j:
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
            res = max(res, min(height[i],height[j])*(j-i))
        return res


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    result = solution.maxArea(height)
    print(result)

