#https://leetcode-cn.com/problems/shortest-completing-word/

"""
如果单词列表（words）中的一个单词包含牌照（licensePlate）中所有的字母，那么我们称之为完整词。在所有完整词中，最短的单词我们称之为最短完整词。
单词在匹配牌照中的字母时不区分大小写，比如牌照中的 "P" 依然可以匹配单词中的 "p" 字母。
我们保证一定存在一个最短完整词。当有多个单词都符合最短完整词的匹配条件时取单词列表中最靠前的一个。
牌照中可能包含多个相同的字符，比如说：对于牌照 "PP"，单词 "pair" 无法匹配，但是 "supper" 可以匹配。

示例 1：
输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
输出："steps"
说明：最短完整词应该包括 "s"、"p"、"s" 以及 "t"。对于 "step" 它只包含一个 "s" 所以它不符合条件。同时在匹配过程中我们忽略牌照中的大小写。
 
示例 2：
输入：licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
输出："pest"
说明：存在 3 个包含字母 "s" 且有着最短长度的完整词，但我们返回最先出现的完整词。
"""


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
        tmp = []
        num = []
        num_1 = []
        licensePlate = licensePlate.lower()
        for i in range(len(licensePlate)):
            if licensePlate[i] in alpha:
                tmp.append(licensePlate[i])

        for j in range(len(words)):
            ans = tmp[:]
            for k in words[j]:
                if k in ans:
                    ans.remove(k)
                else:
                    pass
            if ans == []:
                num.append(words[j])
        for n in range(len(num)):
            num_1.append(len(num[n]))
        return num[num_1.index(min(num_1))]




if __name__ == "__main__":
    licensePlate = "1s3 456"

    words = ["looks","pest","stew","show"]
    solution = Solution()
    result = solution.shortestCompletingWord(licensePlate,words)
    print(result)