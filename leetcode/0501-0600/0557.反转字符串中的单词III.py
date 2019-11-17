#https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/

"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(" ")
        for i in range(len(li)):
            li[i] = li[i][::-1]
        return " ".join(li)

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    solution = Solution()
    result = solution.reverseWords(s)
    print(result)