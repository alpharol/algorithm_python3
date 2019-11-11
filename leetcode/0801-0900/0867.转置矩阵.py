#https://leetcode-cn.com/problems/transpose-matrix/

"""
给定一个矩阵 A， 返回 A 的转置矩阵。
矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：输入：[[1,2,3],[4,5,6],[7,8,9]];输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：输入：[[1,2,3],[4,5,6]];输出：[[1,4],[2,5],[3,6]]
"""

class Solution:
    def transpose(self, A: list):
        if len(A) == 0:
            return []
        else:
            wai_len = len(A)
            nei_len = len(A[0])
            tmp = [[] for _ in range(nei_len)]
            for i in range(nei_len):
                for j in range(wai_len):
                    tmp[i].append(A[j][i])
        return tmp


if __name__ == "__main__":
    A = [[1,2,3],[4,5,6]]
    solution = Solution()
    result = solution.transpose(A)
    print(result)