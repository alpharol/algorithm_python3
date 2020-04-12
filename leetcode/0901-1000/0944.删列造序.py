# https://leetcode-cn.com/problems/delete-columns-to-make-sorted/

"""
给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。

删除 操作的定义是：选出一组要删掉的列，删去 A 中对应列中的所有字符，
形式上，第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）。

示例 1：输入：["cba", "daf", "ghi"] 输出：1
解释：当选择 D = {1}，删除后 A 的列为：["c","d","g"] 和 ["a","f","i"]，均为非降序排列。
若选择 D = {}，那么 A 的列 ["b","a","h"] 就不是非降序排列了。

示例 2：输入：["a", "b"] 输出：0 解释：D = {}

示例 3：输入：["zyx", "wvu", "tsr"] 输出：3 解释：D = {0, 1, 2}
"""

class Solution:
    def minDeletionSize(self, A):
        alphabet = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,
                    "i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,
                    "p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,
                    "w":23,"x":24,"y":25,"z":26}
        num = 0
        for i in range(len(A[0])):
            tmp = [0]
            for j in range(len(A)):
                if alphabet[A[j][i]] >= tmp[j]:
                    tmp.append(alphabet[A[j][i]])
                else:
                    num = num + 1
                    break
        return num

if __name__ == "__main__":
    A = ["cba", "daf", "ghi"]
    solution = Solution()
    result = solution.minDeletionSize(A)
    print(result)


