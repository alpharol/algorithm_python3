#https://leetcode-cn.com/problems/reverse-words-in-a-string/

"""
给定一个字符串，逐个翻转字符串中的每个单词。
示例 1：输入: "the sky is blue";输出: "blue is sky the"

示例 2：输入: "  hello world!  ";输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：输入: "a good   example";输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""


#执行用时 :48 ms, 在所有 Python3 提交中击败了72.58%的用户
#内存消耗 :14.4 MB, 在所有 Python3 提交中击败了5.02%的用户
class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split()
        tmp = tmp[::-1]
        return " ".join(tmp)


if __name__ == "__main__":
    s = "  hello world!  "
    solution = Solution()
    result = solution.reverseWords(s)
    print(result)
