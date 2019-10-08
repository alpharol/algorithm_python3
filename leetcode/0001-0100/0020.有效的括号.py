#https://leetcode-cn.com/problems/valid-parentheses/

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()" 输出: true

示例 2:
输入: "()[]{}" 输出: true

示例 3:
输入: "(]" 输出: false

示例 4:
输入: "([)]" 输出: false

示例 5:
输入: "{[]}" 输出: true
"""


###这种括号的题目就是需要使用栈的思想，也就是数据先进后出
###每次都把左括号加入到stack中，遇到右括号就去找stack里的最末尾元素，也就是栈顶元素
###如果匹配得到的话，那就把栈顶元素删除；如果匹配不到就直接报错
###最后，我们看stack，如果是空列表，就说明正确，如果非空就说明左括号有余
#执行用时 :48 ms, 在所有 Python3 提交中击败了80.82%的用户
#内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.51%的用户
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")": "(", "]": "[", "}": "{"}
        stack = []
        for w in s:
            if w in dict.values():
                stack.append(w)
            else:
                if stack == [] or stack[-1] != dict[w]:
                    return False
                else:
                    stack.pop(-1)
        if stack == []:
            return True
        else:
            return False



if __name__=="__main__":
    s = "((((())))){{{[]}[]}}"
    solution = Solution()
    result = solution.isValid(s)
    print(result)