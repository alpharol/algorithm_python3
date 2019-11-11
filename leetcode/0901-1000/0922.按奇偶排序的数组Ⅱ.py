#https://leetcode-cn.com/problems/sort-array-by-parity-ii/

"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。

示例：输入：[4,2,5,7];输出：[4,5,2,7];解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
"""

class Solution:
    def sortArrayByParityII(self, A: list):
        ji = []
        ou = []
        for a in A:
            if a % 2 == 0:
                ou.append(a)
            else:
                ji.append(a)
        ans = []
        for j in range(len(ji)):
            ans.append(ou[j])
            ans.append(ji[j])
        return ans

if __name__ == "__main__":
    A = [4,2,5,7]
    solution = Solution()
    result = solution.sortArrayByParityII(A)
    print(result)