#https://leetcode-cn.com/problems/reverse-string-ii/

"""
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:输入: s = "abcdefg", k = 2;输出: "bacdfeg"
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        batch = int(len(s)/k)+1
        li = list(s)
        for w in range(batch):
            if w % 2 == 0:
                tmp = li[w*k:(w+1)*k]
                tmp.reverse()
                li[w*k:(w+1)*k] = tmp
        return "".join(li)

if __name__ == "__main__":
    s = "abcdefghijk"
    k = 2
    solution = Solution()
    result = solution.reverseStr(s,k)
    print(result)