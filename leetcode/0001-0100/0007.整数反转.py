# https://leetcode-cn.com/problems/reverse-integer/

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

#将本题目分成三种情况讨论：负数u，零和正数，需要额外考虑在反转之后0开头的情况，具体的反转可以使用字符串操作。
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)[1:]
            x = x[::-1].lstrip("0")
            if int(x) > 2 ** 31:
                return 0
            else:
                return int("-" + x)
        elif x == 0:
            return 0
        else:
            x = str(x)[::-1].lstrip("0")
            if int(x) >= 2 ** 31:
                return 0
            else:
                return int(x)


if __name__ == "__main__":
    x = -123
    solution = Solution()
    result = solution.reverse(x)
    print(result)
