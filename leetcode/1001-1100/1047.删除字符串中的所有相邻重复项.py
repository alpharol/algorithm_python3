#https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/

"""
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：输入："abbaca";输出："ca"

例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
"""



#************************************#
#*************solution 1*************#
#************************************#
#这道题目用栈的思想更好一点
#执行用时 :116 ms, 在所有 Python3 提交中击败了62.30%的用户
#内存消耗 :13.9 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def removeDuplicates(self, S):
        s_li = list(S)
        ans = []
        for w in s_li:
            if len(ans) == 0:
                ans.append(w)
            else:
                if ans[-1] == w:
                    ans.pop(-1)
                else:
                    ans.append(w)
        return "".join(ans)


if __name__ == "__main__":
    S = "aaaa"
    solution = Solution()
    result = solution.removeDuplicates(S)
    print(result)
