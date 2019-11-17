#https://leetcode-cn.com/problems/reverse-vowels-of-a-string/

"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
示例 1:输入: "hello";输出: "holle"
示例 2:输入: "leetcode";输出: "leotcede"
说明:
元音字母不包含字母"y"。
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        yuan = []
        ans = []
        for i in range(len(s)):
            if s[i] in ["a","e","i","o","u","A","E","I","O","U"]:
                ans.append(0)
                yuan.append(s[i])
            else:
                ans.append(s[i])
        yuan.reverse()
        for j in range(len(ans)):
            if ans[j] == 0:
                ans[j] = yuan[0]
                yuan.pop(0)
        return "".join(ans)


if __name__ == "__main__":
    s = "Aa"
    solution = Solution()
    result = solution.reverseVowels(s)
    print(result)
