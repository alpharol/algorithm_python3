#https://leetcode-cn.com/problems/relative-sort-array/

"""
给你两个数组，arr1 和 arr2，
arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。
未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
"""

#执行用时 :72 ms, 在所有 Python3 提交中击败了33.05%的用户
#内存消耗 :13.8 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def relativeSortArray(self, arr1, arr2):
        ex = []      #保存在arr2中出现的
        no_ex = []   #保存没在arr2中出现的
        for w in arr1:
            if w in arr2:
                ex.append(w)
            else:
                no_ex.append(w)
        ###处理no_ex
        no_ex.sort()
        ###处理ex
        ans = []
        for a in arr2:
            tmp = ex.count(a)
            ans = ans + [a] * tmp
        ans = ans + no_ex
        return ans

if __name__ == "__main__":
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2, 1, 4, 3, 9, 6]
    solution = Solution()
    result = solution.relativeSortArray(arr1,arr2)
    print(result)

