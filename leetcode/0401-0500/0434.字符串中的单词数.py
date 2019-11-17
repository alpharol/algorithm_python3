#https://leetcode-cn.com/problems/number-of-segments-in-a-string/

"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:输入: "Hello, my name is John";输出: 5
"""

class Solution:
    def countSegments(self, s: str) -> int:
        if s == "":
            return 0
        else:
            k = s.split(" ")
            count = 0
            for w in k:
                if w != "":
                    count = count + 1
            return count

if __name__ == "__main__":
    s = "    "
    solution = Solution()
    result = solution.countSegments(s)
    print(result)