#https://leetcode-cn.com/problems/valid-anagram/

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
示例 1:输入: s = "anagram", t = "nagaram";输出: true
示例 2:输入: s = "rat", t = "car";输出: false
"""

class Solution(object):
    def isAnagram(self, s, t):
        dict_1 = {}
        dict_2 = {}
        for m in s:
            if m not in dict_1:
                dict_1[m] = 1
            else:
                dict_1[m] = dict_1[m] + 1
        for n in t:
            if n not in dict_2:
                dict_2[n] = 1
            else:
                dict_2[n] = dict_2[n] + 1
        if dict_1 == dict_2:
            return True
        else:
            return False

if __name__ == "__main__":
    s = "rat"
    t = "car"
    solution = Solution()
    result = solution.isAnagram(s,t)
    print(result)