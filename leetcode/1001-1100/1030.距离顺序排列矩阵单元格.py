#https://leetcode-cn.com/problems/matrix-cells-in-distance-order/

"""
给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。
返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，
其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。
（你可以按任何满足此条件的顺序返回答案。）

示例 1：输入：R = 1, C = 2, r0 = 0, c0 = 0;输出：[[0,0],[0,1]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1]

示例 2：输入：R = 2, C = 2, r0 = 0, c0 = 1;输出：[[0,1],[0,0],[1,1],[1,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2] [[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。

示例 3：输入：R = 2, C = 3, r0 = 1, c0 = 2;输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
"""

"""
##########这个方法应该是可以的，但是超出了时间限制
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        unit_coordinate = []
        distance = []
        for i in range(R):
            for j in range(C):
                tmp_coordinate = [i,j]
                tmp_dis = abs(i-r0)+abs(j-c0)
                unit_coordinate.append(tmp_coordinate)
                distance.append(tmp_dis)
        tmp = [0] * (R * C)
        for i in range(len(distance)):
            index = distance.index(min(distance))
            tmp[i] = unit_coordinate[index]
            distance.pop(index)
            unit_coordinate.pop(index)

        return tmp
"""


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        tmp = []
        for i in range(R):
            for j in range(C):
                tmp = tmp + [[abs(i-r0)+abs(j-c0),i,j]]

        ans = sorted(tmp,key=(lambda x:x[0]))
        for i in range(len(ans)):
            ans[i] = ans[i][1:]
        return ans

if __name__ == "__main__":
    R = 2; C = 3; r0 = 1; c0 = 2
    solution = Solution()
    result = solution.allCellsDistOrder(R,C,r0,c0)
    print(result)