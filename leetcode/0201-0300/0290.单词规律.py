#https://leetcode-cn.com/problems/word-pattern/submissions/

"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:输入: pattern = "abba", str = "dog cat cat dog";输出: true
示例 2:输入:pattern = "abba", str = "dog cat cat fish";输出: false
示例 3:输入: pattern = "aaaa", str = "dog cat cat dog";输出: false
示例 4:输入: pattern = "abba", str = "dog dog dog dog";输出: false
"""

class Solution:
    def wordPattern(self, pattern, str):
        list_str = str.split(" ")
        dict = {}
        if len(set(pattern)) != len(set(list_str)):
            return False
        if len(pattern) != len(list_str):
            return False
        else:
            for i in range(len(pattern)):
                if pattern[i] not in dict:
                    dict[pattern[i]] = list_str[i]
                else:
                    if dict[pattern[i]] != list_str[i]:
                        return False
            return True

if __name__ == "__main__":
    pattern = "aba"
    str = "cat cat cat dog"
    solution = Solution()
    result = solution.wordPattern(pattern,str)
    print(result)