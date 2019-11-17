# https://leetcode-cn.com/problems/fizz-buzz/

"""
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
示例：n = 15,
返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution:
    def fizzBuzz(self, n: int):
        ans = []
        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
               ans.append("FizzBuzz")
            elif (i + 1) % 3 == 0:
                ans.append("Fizz")
            elif (i+1)%5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i+1))
        return ans

if __name__ == "__main__":
    n = 15
    solution =Solution()
    result = solution.fizzBuzz(n)
    print(result)