# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
###这里需要使用滑窗的思想：
#如果没有重复的话，我们就把这个字符加进去
#如果重复了的话，我们就找到之前的字符，然后把这个字符之前包括这个字符都删掉，然后添加上这个字符
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            tmp, length = [], []
            for i in range(len(s)):
                #print(s[i])
                if s[i] not in tmp:
                    tmp.append(s[i])
                    length.append(len(tmp))
                else:
                    index = tmp.index(s[i])
                    tmp = tmp[index+1:]
                    tmp.append(s[i])
                    length.append(len(tmp))
                #print(tmp)
            return max(length)

if __name__ == "__main__":
    s = "pwwkew"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))



