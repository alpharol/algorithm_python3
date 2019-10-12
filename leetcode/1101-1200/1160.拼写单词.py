#https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/

"""
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。

示例 1：输入：words = ["cat","bt","hat","tree"], chars = "atach";输出：6
解释： 可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

示例 2：输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr";输出：10
解释：可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
"""

#执行用时 :324 ms, 在所有 Python3 提交中击败了42.25%的用户
#内存消耗 :14.1 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def countCharacters(self, words, chars) -> int:
        dict = {}
        for w in chars:
            if w not in dict:
                dict[w] = 1
            else:
                dict[w] = dict[w] + 1
        x = 0
        for i in range(len(words)):
            tmp = {}
            flag = True
            for q in words[i]:
                if q not in tmp:
                    tmp[q] = 1
                else:
                    tmp[q] = tmp[q] + 1
            for t in tmp:
                if t not in dict or tmp[t] > dict[t]:
                    flag = False
            if flag:
                x = x + len(words[i])
        return x

if __name__ == "__main__":
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    solution = Solution()
    result = solution.countCharacters(words,chars)
    print(result)
