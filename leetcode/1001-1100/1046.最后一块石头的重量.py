#https://leetcode-cn.com/problems/last-stone-weight/

"""
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。
那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
"""


#执行用时 :44 ms, 在所有 Python3 提交中击败了84.08%的用户
#内存消耗 :13.9 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def lastStoneWeight(self, stones: list):
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones[-1] = stones[-1] - stones[-2]
                stones.pop(-2)
        if len(stones) != 0:
            return stones[0]
        else:
            return 0

if __name__ == "__main__":
    stones = [1,2,3,4,6,9]
    solution = Solution()
    result = solution.lastStoneWeight(stones)
    print(result)