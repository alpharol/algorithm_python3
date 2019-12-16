# https://leetcode-cn.com/problems/implement-trie-prefix-tree/

"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
"""

# 执行用时 :136 ms, 在所有 python3 提交中击败了97.62%的用户
# 内存消耗 :27.4 MB, 在所有 python3 提交中击败了41.22%的用户
class Trie:
    def __init__(self):
        self.dic = {}

    def insert(self, strr):
        a = self.dic
        for i in strr:
            if i not in a:
                a[i] = {}
            # 这个地方有没有else是不一样的！！！
            a = a[i]
        a["end"] = True

    def search(self, strr):
        a = self.dic
        for i in strr:
            if i not in a:
                return False
            else:
                a = a[i]
        if "end" in a:
            return True
        else:
            return False

    def startsWith(self, strr):
        a = self.dic
        for i in strr:
            if i not in a:
                return False
            else:
                a = a[i]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
