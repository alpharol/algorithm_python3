#https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array/

"""
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
返回重复了 N 次的那个元素。
示例 1：输入：[1,2,3,3]；输出：3
示例 2：输入：[2,1,2,5,3,2]；输出：2
示例 3：输入：[5,1,5,2,5,3,5,4];输出：5
"""
###使用dict方法
#执行用时 :308 ms, 在所有 Python3 提交中击败了8.56%的用户
#内存消耗 :15.1 MB, 在所有 Python3 提交中击败了5.08%的用户
"""
class Solution:
    def repeatedNTimes(self, A: list):
        dict = {}
        for w in A:
            if w in dict.keys():
                return w
            else:
                dict[w] = 1
"""

###几乎一样的速度还是很慢
class Solution:
    def repeatedNTimes(self, A: list):
        a = set()
        for w in A:
            if w not in a:
                a.add(w)
            else:
                return w

if __name__ == "__main__":
    A = [5,1,5,2,5,3,5,4]
    solution =Solution()
    result = solution.repeatedNTimes(A)
    print(result)