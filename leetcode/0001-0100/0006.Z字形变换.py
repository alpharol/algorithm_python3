#https://leetcode-cn.com/problems/zigzag-conversion/

"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：string convert(string s, int numRows);

示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3   输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4   输出: "LDREOEIIECIHNTSG"

解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == "":
            return ""
        if numRows == 1:
            return s
        else:
            row_index = []
            for i in range(numRows):
                row_index.append(i+1)
            for j in range(numRows-1,1,-1):
                row_index.append(j)
            m = len(s) % len(row_index)
            n = len(s) // len(row_index)
            index = row_index*n + row_index[:m]
            alpha_row = [[] for _ in range(numRows)]
            for i in range(len(s)):
                alpha_row[int(index[i]-1)].append(s[i])
            tmp = ""
            for i in range(len(alpha_row)):
                ans = "".join(alpha_row[i])
                tmp = tmp + ans
            #ans = "".join(alpha_row)
            return tmp

if __name__ == "__main__":
    s = "LEETCODEISHIRING"
    numRows = 4
    solution = Solution()
    result = solution.convert(s,numRows)
    print(result)