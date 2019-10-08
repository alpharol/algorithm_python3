#https://leetcode-cn.com/problems/repeated-dna-sequences/

"""
所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。
在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。

示例:输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";输出: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str):
        n = len(s)-9
        dict = {}
        for i in range(n):
            if s[i:i+10] in dict.keys():
                dict[s[i:i+10]] = True
            else:
                dict[s[i:i + 10]] = False
        ans = []
        for i in dict:
            if dict[i]:
                ans.append(i)
            else:
                pass
        return ans

if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    solution = Solution()
    result = solution.findRepeatedDnaSequences(s)
    print(result)
