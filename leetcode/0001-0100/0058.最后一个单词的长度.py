#https://leetcode-cn.com/problems/length-of-last-word/

"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:
输入: "Hello World" 输出: 5
"""
# ************************************#
# *************solution 2*************#
# ************************************#
#这是一个O(1)的算法
#执行用时 :44 ms, 在所有 Python3 提交中击败了87.74%的用户
#内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.01%的用户
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip().lstrip()
        ans = s.split(" ")
        return len(ans[-1])

if __name__ == "__main__":
    s = "a "
    solution = Solution()
    result = solution.lengthOfLastWord(s)
    print(result)



# ************************************#
# *************solution 1*************#
# ************************************#
#时间复杂度O(n)
#执行用时 :84 ms, 在所有 Python3 提交中击败了9.17%的用户
#内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.01%的用户
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        ans = []
        for w in s:
            if w != " ":
                ans.append(w)
            else:
                ans = []
        return len(ans)
"""