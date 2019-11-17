#https://leetcode-cn.com/problems/first-unique-character-in-a-string/

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
案例:s = "leetcode"返回 0.
s = "loveleetcode",返回 2.
"""
#import collections
# ************************************#
# *************solution 1*************#
# ************************************#
#使用哈希表
#执行用时 :152 ms, 在所有 Python3 提交中击败了69.81%的用户
#内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.34%的用户
"""
class Solution:
    def firstUniqChar(self, s):
        #count = collections.Counter(s)
        count = {}
        for ch in s:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] = count[ch] + 1
        print(count)
        # find the index
        index = 0
        for ch in s:
            if count[ch] == 1:
                return index
            else:
                index += 1
        return -1
"""


# ************************************#
# *************solution 2*************#
# ************************************#
#还是哈希表比较快
#执行用时 :496 ms, 在所有 Python3 提交中击败了7.99%的用户
#内存消耗 :14.4 MB, 在所有 Python3 提交中击败了5.34%的用户
class Solution:
    def firstUniqChar(self, s):
        s_li = list(s)
        re = []
        for i in range(len(s_li)):
            if s_li[i] not in re and s_li.count(s_li[i]) == 1:
                return i
            else:
                re.append(s_li[i])
        return -1

if __name__ == "__main__":
    s = "leetcode"
    solution = Solution()
    result = solution.firstUniqChar(s)
    print(result)
