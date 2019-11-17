#https://leetcode-cn.com/problems/detect-capital/

"""
给定一个单词，你需要判断单词的大写使用是否正确。
我们定义，在以下情况时，单词的大写用法是正确的：
全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:输入: "USA";输出: True
示例 2:输入: "FlaG";输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","L","M","N","O","P","Q","R","S","T","U",
                 "V","W","X","Y","Z"]
        tmp = []
        for i in range(len(word)):
            if word[i] in alpha:
                tmp.append(i)
        if len(tmp) == 0:
		# 都是小写字母
            return True
        elif len(tmp) == 1:
            if tmp[0] == 0:
			# 只有首字母大写
                return True
            else:
                return False
        else:
            if len(tmp) == len(word):
			# 所有字母都是大写
                return True
            else:
                return False

if __name__ == "__main__":
    word = "FlaG"
    solution = Solution()
    result = solution.detectCapitalUse(word)
    print(result)

