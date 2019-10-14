#https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/

"""
给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
形式上，如果我们可以找出索引 i+1 < j 
且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

示例 1：输出：[0,2,1,-6,6,-7,9,1,2,0,1];输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

示例 2：输入：[0,2,1,-6,6,7,9,-1,2,0,1];输出：false

示例 3：输入：[3,3,6,5,-2,2,5,1,-9,4];输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
"""

#执行用时 :484 ms, 在所有 Python3 提交中击败了5.02%的用户
#内存消耗 :20.5 MB, 在所有 Python3 提交中击败了5.17%的用户
class Solution:
    def canThreePartsEqualSum(self, A: list):
        tmp = sum(A)/3
        if int(tmp) != tmp:
            return False
        else:
            count = 0
            for w in A:
                count = count + w
                if count == tmp:
                    count = 0
                else:
                    pass
        if count != 0:
            return False
        else:
            return True


if __name__ == "__main__":
    A = [3,3,6,5,-2,2,5,1,-9,4]
    solution = Solution()
    result = solution.canThreePartsEqualSum(A)
    print(result)