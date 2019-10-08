# https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""


# 25ms+5836k
###这道题目其实也是斐波那契数列的题目，但是需要注意的是这个问题问得是总共有多少种方法跳上去
class Solution:
    def jumpFloor(self, number):
        ans = [1, 2]
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            k = number - 2
            while k > 0:
                ans.append(ans[-1] + ans[-2])
                k = k - 1
            return ans[-1]


if __name__ == "__main__":
    number = 5
    solution = Solution()
    result = solution.jumpFloor(number)
    print(result)