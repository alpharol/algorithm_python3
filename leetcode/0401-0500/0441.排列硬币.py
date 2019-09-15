#https://leetcode-cn.com/problems/arranging-coins/

"""
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
给定一个数字 n，找出可形成完整阶梯行的总行数。
n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:n = 5
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤
因为第三行不完整，所以返回2.

示例 2:n = 8
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
因为第四行不完整，所以返回3.
"""

# ************************************#
# *************solution 2*************#
# ************************************#
###数学方法
#执行用时 :44 ms, 在所有 Python3 提交中击败了98.52%的用户
#内存消耗 :14 MB, 在所有 Python3 提交中击败了5.41%的用户
class Solution:
    def arrangeCoins(self, n: int) -> int:
        import math
        return int((math.sqrt(8*n+1)-1)/2)
if __name__ == "__main__":
    n = 3
    solution = Solution()
    result = solution.arrangeCoins(n)
    print(result)



# ************************************#
# *************solution 1*************#
# ************************************#
###这个方法是O(n)的方法
#执行用时 :1188 ms, 在所有 Python3 提交中击败了31.73%的用户
#内存消耗 :14 MB, 在所有 Python3 提交中击败了5.41%的用户
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            row = 2
            count = 1
            while count <= n:
                #print(row)
                count = count + row
                row = row + 1
            return row-2
"""