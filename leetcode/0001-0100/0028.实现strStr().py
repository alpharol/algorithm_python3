#https://leetcode-cn.com/problems/implement-strstr/

"""
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""
#执行用时 :44 ms, 在所有 Python3 提交中击败了92.24%的用户
#内存消耗 :13.1 MB, 在所有 Python3 提交中击败了94.43%的用户
###使用移动滑窗的思想
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(h-n+1):
            if haystack[i:i+n] != needle:
                pass
            else:
                return i
        return -1

if __name__=="__main__":
    haystack = "hello"
    needle = "ll"
    solution = Solution()
    result = solution.strStr(haystack,needle)
    print(result)