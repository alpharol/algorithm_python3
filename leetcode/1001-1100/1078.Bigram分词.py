#https://leetcode-cn.com/problems/occurrences-after-bigram/

"""
给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，
其中 second 紧随 first 出现，third 紧随 second 出现。
对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

示例 1：
输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]

示例 2：
输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]
"""


#执行用时 :52 ms, 在所有 Python3 提交中击败了46.05%的用户
#内存消耗 :14 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        tmp = []
        ans = []
        for w in text.split(" "):
            tmp.append(w)
        for i in range(len(tmp)-2):
            if tmp[i] == first and tmp[i+1] == second:
                ans.append(tmp[i+2])
        return ans

if __name__ == "__main__":
    text = "we will we will rock you"
    first = "we"
    second = "will"
    solution = Solution()
    result = solution.findOcurrences(text,first,second)
    print(result)
