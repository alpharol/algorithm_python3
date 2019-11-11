#https://leetcode-cn.com/problems/self-dividing-numbers/

"""
自除数 是指可以被它包含的每一位数除尽的数。
例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
还有，自除数不允许包含 0 。
给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：输入： 上边界left = 1, 下边界right = 22;输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        ans = []
        for i in range(left,right+1):
            status = True
            if "0" in str(i):
                status = False
                pass
            else:
                for s in str(i):
                    if i % int(s) != 0:
                        status = False
                        break
            if status:
                ans.append(i)
        return ans


if __name__ == "__main__":
    left = 1
    right = 22
    solution = Solution()
    result = solution.selfDividingNumbers(left,right)
    print(result)

