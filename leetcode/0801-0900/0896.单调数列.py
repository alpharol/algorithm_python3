#https://leetcode-cn.com/problems/monotonic-array/

"""
如果数组是单调递增或单调递减的，那么它是单调的。
如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。
如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。

示例 1：输入：[1,2,2,3];输出：true
示例 2：输入：[6,5,4,4];输出：true
示例 3：输入：[1,3,2];输出：false
示例 4：输入：[1,2,4,5];输出：true
示例 5：输入：[1,1,1];输出：true
"""


class Solution:
    def isMonotonic(self, A: list):
        if len(A) <= 1:
            return True
        else:
            if max(A) == A[0]:
                for i in range(len(A)-1):
                    if A[i] < A[i+1]:
                        return False
                return True
            elif min(A) == A[0]:
                for i in range(len(A)-1):
                    if A[i] > A[i+1]:
                        return False
                return True
            else:
                return False


if __name__ == "__main__":
    A = [1,1,1]
    solution =Solution()
    result = solution.isMonotonic(A)
    print(result)

