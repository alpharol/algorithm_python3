#https://leetcode-cn.com/problems/find-the-difference/

"""
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例:输入：s = "abcd"t = "abcde";输出：e
解释：'e' 是那个被添加的字母。
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_li = list(s)
        t_li = list(t)
        s_li.sort()
        t_li.sort()
        for i in range(len(s_li)):
            if s_li[i] != t_li[i]:
                return t_li[i]
        return t_li[-1]

if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    solution = Solution()
    result = solution.findTheDifference(s,t)
    print(result)
