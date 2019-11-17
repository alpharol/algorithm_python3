#https://leetcode-cn.com/problems/keyboard-row/

"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
示例：
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
"""

class Solution:
    def findWords(self, words: list):
        res = []
        first = ["q","w","e","r","t","y","u","i","o","p","Q","W","E","R","T","Y","U","I","O","P"]
        second = ["a","s","d","f","g","h","j","k","l","A","S","D","F","G","H","J","K","L"]
        third = ["z","x","c","v","b","n","m","Z","X","C","V","B","N","M"]
        for i in range(len(words)):
            tmp = []
            for w in words[i]:
                if w in first:
                    tmp.append(1)
                elif w in second:
                    tmp.append(2)
                else:
                    tmp.append(3)
            if len(set(tmp)) == 1:
                res.append(words[i])
        return res


if __name__ == "__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    solution = Solution()
    result = solution.findWords(words)
    print(result)


