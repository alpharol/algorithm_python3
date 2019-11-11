#https://leetcode-cn.com/problems/powerful-integers/solution/python-by-agl66/

"""
给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
返回值小于或等于 bound 的所有强整数组成的列表。
你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

示例 1：输入：x = 2, y = 3, bound = 10;输出：[2,3,4,5,7,9,10]
示例 2：输入：x = 3, y = 5, bound = 15;输出：[2,4,6,8,10,14]

提示：1 <= x <= 100;1 <= y <= 100;0 <= bound <= 10^6
"""

class Solution:
    def powerfulIntegers(self, x, y, bound):
        import math
        if x == 1 and y != 1:
            b = int(math.log(bound, y)) + 1
            ans = []
            for i in range(b):
                tmp = 1 + y**i
                if tmp <= bound:
                    ans.append(tmp)
            return list(set(ans))
        elif x != 1 and y == 1:
            a = int(math.log(bound,x))+1
            ans = []
            for i in range(a):
                tmp = 1 + x**i
                if tmp <= bound:
                    ans.append(tmp)
            return list(set(ans))
        elif x == 1 and y == 1:
            if bound > 1:
                return [2]
            else:
                return []
        else:
            a = int(math.log(bound, x)) + 1
            b = int(math.log(bound,y))+1
            ans = []
            for i in range(a):
                for j in range(b):
                    tmp = x**i + y**j
                    if tmp <= bound:
                        ans.append(tmp)
            return list(set(ans))



if __name__ == "__main__":
    x = 1
    y = 3
    bound = 15
    solution = Solution()
    result = solution.powerfulIntegers(x,y,bound)
    print(result)