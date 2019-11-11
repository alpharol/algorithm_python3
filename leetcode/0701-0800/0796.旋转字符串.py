#https://leetcode-cn.com/problems/rotate-string/

"""
给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。

示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true

示例 2:
输入: A = 'abcde', B = 'abced'
输出: false
"""

class Solution:
    def rotateString(self, A: str, B: str):
        if A == "" and B == "":
            return True
        if A == "" and B != "":
            return False
        tmp = []
        for i in range(len(A)):
            a = A[1:]+A[0]
            tmp.append(a)
            A = a
        #print(tmp)
        if B in tmp:
            return True
        else:
            return False


if __name__ == "__main__":
    A = "abcde"
    B = "abced"
    solution = Solution()
    result = solution.rotateString(A,B)
    print(result)

