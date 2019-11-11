#https://leetcode-cn.com/problems/squares-of-a-sorted-array/

"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：输入：[-4,-1,0,3,10];输出：[0,1,9,16,100]
示例 2：输入：[-7,-3,2,3,11];输出：[4,9,9,49,121]
"""



class Solution:
    def sortedSquares(self, A):
        abs = []
        for i in range(len(A)):
            abs.append(A[i]**2)
        abs.sort()
        return abs

if __name__ == "__main__":
    A = [-4, -1, 0, 3, 10]
    solution = Solution()
    result = solution.sortedSquares(A)
    print(result)