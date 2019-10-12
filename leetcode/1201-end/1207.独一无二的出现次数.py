#https://leetcode-cn.com/problems/unique-number-of-occurrences/

"""
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

示例 1：输入：arr = [1,2,2,1,1,3];输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。

示例 2：输入：arr = [1,2];输出：false

示例 3：输入：arr = [-3,0,1,-3,1,1,1,-3,10,0];输出：true
 
提示：
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

#执行用时 :48 ms, 在所有 Python3 提交中击败了73.45%的用户
#内存消耗 :13.9 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        dict = {}
        for i in range(len(arr)):
            if arr[i] not in dict:
                dict[arr[i]] = 1
            else:
                dict[arr[i]] = dict[arr[i]] + 1
        return len(dict.values()) == len(set(list(dict.values())))


if __name__ == "__main__":
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    solution = Solution()
    result = solution.uniqueOccurrences(arr)
    print(result)