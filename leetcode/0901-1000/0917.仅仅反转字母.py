#https://leetcode-cn.com/problems/reverse-only-letters/

"""
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：输入："ab-cd";输出："dc-ba"
示例 2：输入："a-bC-dEf-ghIj";输出："j-Ih-gfE-dCba"
示例 3：输入："Test1ng-Leet=code-Q!";输出："Qedo1ct-eeLg=ntse-T!"
"""

class Solution:
    def reverseOnlyLetters(self, S: str):
        alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                 "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        alpha_list = []
        symbol = []
        symbol_index = []
        for i in range(len(S)):
            if S[i] in alpha:
                alpha_list.append(S[i])
            else:
                symbol_index.append(i)
                symbol.append(S[i])

        rever = alpha_list[::-1]
        # print(rever)
        # print(symbol)
        # print(symbol_index)
        ans = []
        for j in range(len(S)):
            if j in symbol_index:
                ans.append(symbol[0])
                symbol.pop(0)
            else:
                ans.append(rever[0])
                rever.pop(0)
        # print(ans)
        return "".join(ans)

if __name__ == "__main__":
    S = "Test1ng-Leet=code-Q!"
    solution = Solution()
    result = solution.reverseOnlyLetters(S)
    print(result)
