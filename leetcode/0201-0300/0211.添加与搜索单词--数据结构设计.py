#https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/

"""
设计一个支持以下两种操作的数据结构：
void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""

class WordDictionary:

    def __init__(self):
        #Initialize your data structure here.
        self.dic = {}

    def addWord(self, word: str) -> None:
        #Adds a word into the data structure.
        a = self.dic
        n = len(word)
        if n in a:
            a[n] = a[n] + [word]
        else:
            a[n] = [word]
        #print(a)

    def search(self, word: str) -> bool:
        #Returns if the word is in the data structure.
        # A word could contain the dot character . to represent any one letter.
        a = self.dic
        n = len(word)

        def match(s):
            for i in range(n):
                if s[i] != word[i] and word[i] != ".":
                    return False
            return True

        if n not in a:
            return False
        else:
            for w in a[n]:
                if match(w):
                    return True
            return False


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad"))
    print(wd.search("bad"))
    print(wd.search(".ad"))
    print(wd.search("b.."))
    print(wd.search("b.p"))