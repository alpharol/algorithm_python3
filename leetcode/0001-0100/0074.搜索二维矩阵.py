#https://leetcode-cn.com/problems/search-a-2d-matrix/

"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
"""

#执行用时 :72 ms, 在所有 Python 提交中击败了56.69%的用户
#内存消耗 :13.5 MB, 在所有 Python 提交中击败了=44.07%的用户
##这个算法是O(M*N)
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False
"""

#执行用时 :72 ms, 在所有 Python 提交中击败了56.69%的用户
#内存消耗 :13.4 MB, 在所有 Python 提交中击败了48.15%的用户
#二分查找
class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] < target:
                left,right = 0,len(matrix[0])-1
                while left <= right:
                    mid = int((left+right)/2)
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
        return False

if __name__ == "__main__":
    matrix =  [[1],[3]]
    target = 3
    solution = Solution()
    result = solution.searchMatrix(matrix,target)
    print(result)