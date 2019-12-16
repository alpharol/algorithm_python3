# https://leetcode-cn.com/problems/replace-words/

"""
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。
例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。
如果继承词有许多可以形成它的词根，则用最短的词根替换它。
你需要输出替换之后的句子。

示例 1:
输入: dict(词典) = ["cat", "bat", "rat"]
sentence(句子) = "the cattle was rattled by the battery"
输出: "the cat was rat by the bat"
"""
####使用内置函数startwith
# 执行用时 :192 ms, 在所有 python3 提交中击败了58.46%的用户
# 内存消耗 :18.5 MB, 在所有 python3 提交中击败了30.61%的用户
"""
class Solution:
    def replaceWords(self, dict: list, sentence: str) -> str:
        dict.sort()
        s = sentence.split(' ')
        for i, word in enumerate(s):
            for j in dict:
                if word.startswith(j):
                    s[i] = j
                    break
        return ' '.join(s)
"""


###使用字典树
# 执行用时 :96 ms, 在所有 Python3 提交中击败了80.43%的用户
# 内存消耗 :27.8 MB, 在所有 Python3 提交中击败了18.37%的用户
class Solution:
    def replaceWords(self, dict: list, sentence: str) -> str:
        d = {}
        # 一定是需要一个额外的t字典的，如果不存在的话，那每次最后都是{“end”:True}
        for word in dict:
            t = d
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["end"] = True

        def fnd(word: list):
            t = d
            for i, c in enumerate(word):
                if "end" in t:
                    return word[:i]
                elif c in t:
                    t = t[c]
                else:
                    return word

        return " ".join(map(fnd, sentence.split(" ")))


if __name__ == "__main__":
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    solution = Solution()
    result = solution.replaceWords(dict, sentence)
    print(result)
