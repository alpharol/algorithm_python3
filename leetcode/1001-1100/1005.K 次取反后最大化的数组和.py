# https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/

"""
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个个索引 i 并将 A[i] 替换为 -A[i]，
然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）
以这种方式修改数组后，返回数组可能的最大和。

示例 1：输入：A = [4,2,3], K = 1  输出：5 解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。

示例 2：输入：A = [3,-1,0,2], K = 3 输出：6 解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。

示例 3：输入：A = [2,-3,-1,5,-4], K = 2 输出：13 解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
"""
#执行用时 :56 ms, 在所有 Python3 提交中击败了82.82%的用户
#内存消耗 :13.7 MB, 在所有 Python3 提交中击败了11.11%的用户
#这段代码真的是又臭又长，我分出了所有的情况对其进行讨论，太麻烦了。
# ************************************#
# *************solution 1*************#
# ************************************#
"""
class Solution:
    def largestSumAfterKNegations(self, A, K) -> int:
        a = 0
        for i in range(len(A)):
            if A[i] < 0:
                a = a + 1
        if 0 in A:
            if a <= K:
                num = 0
                for i in range(len(A)):
                    num = num + abs(A[i])
                return num
            else:
                A_s = sorted(A)
                flag = 0
                while flag < K:
                    A_s[flag] = abs(A_s[flag])
                    flag = flag + 1
                return sum(A_s)
        else:
            if a < K:
                if (K-a)%2 == 0:
                    num = 0
                    for i in range(len(A)):
                        num = num + abs(A[i])
                    return num
                else:
                    num = 0
                    for i in range(len(A)):
                        A[i] = abs(A[i])
                    return sum(A)-2*min(A)
            elif a == K:
                num = 0
                for i in range(len(A)):
                    num = num + abs(A[i])
                return num
            else:
                A_s = sorted(A)
                flag = 0
                while flag < K:
                    A_s[flag] = abs(A_s[flag])
                    flag = flag + 1
                return sum(A_s)
"""


#执行用时 :88 ms, 在所有 Python3 提交中击败了37.88%的用户
#内存消耗 :13.7 MB, 在所有 Python3 提交中击败了11.11%的用户
#这段代码真的是又臭又长，我分出了所有的情况对其进行讨论，太麻烦了。
# ************************************#
# *************solution 2*************#
# ************************************#
#这段代码真的是简洁漂亮，而且很漂亮的使用了贪心算法
class Solution:
    def largestSumAfterKNegations(self, A, K) -> int:
        for i in range(K):
            A = sorted(A)
            A[0] = -A[0]
        return sum(A)


if __name__ == "__main__":
    A = [-28,-19,-13,5,-12,-27,0,29,-2,-6]
    K = 2
    solution = Solution()
    result = solution.largestSumAfterKNegations(A,K)
    print(result)