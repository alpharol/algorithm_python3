#https://leetcode-cn.com/problems/fibonacci-number/solution/

"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。
该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

示例 1：输入：2;输出：1;解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：输入：3;输出：2;解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：输入：4;输出：3;解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
"""

# ************************************#
# *************solution 1*************#
# ************************************#
"""
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        dict = {0:0,1:1}
        i = 2
        while i < N:
            dict[i] = dict[i-1]+dict[i-2]
            i = i + 1
        return dict[N-1]+dict[N-2]
"""

# ************************************#
# *************solution 2*************#
# ************************************#
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        li = [0,1]
        i = 2
        while i < N:
            li.append(li[i-1]+li[i-2])
            i = i + 1
        return li[-1]+li[-2]

if __name__ == "__main__":
    N = 1
    solution = Solution()
    result = solution.fib(N)
    print(result)