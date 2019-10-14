#https://leetcode-cn.com/problems/duplicate-zeros/

"""
给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
注意：请不要在超过该数组长度的位置写入元素。
要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。

示例 1：输入：[1,0,2,3,0,4,5,0]输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

示例 2：输入：[1,2,3]输出：null
解释：调用函数后，输入的数组将被修改为：[1,2,3]
"""

#执行用时 :112 ms, 在所有 Python3 提交中击败了34.67%的用户
#内存消耗 :14.4 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n-1:
            if arr[i] != 0:
                i = i + 1
            else:
                arr.pop(-1)
                arr.insert(i,0)
                i = i + 2
        arr = arr[:n]

if __name__ == "__main__":
    arr = [1,2,3]
    solution = Solution()
    solution.duplicateZeros(arr)
    print(arr)