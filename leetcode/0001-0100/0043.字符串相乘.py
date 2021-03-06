#https://leetcode-cn.com/problems/multiply-strings/

"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
示例 1:输入: num1 = "2", num2 = "3"输出: "6"
示例 2:输入: num1 = "123", num2 = "456"输出: "56088"
说明：
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""


class Solution(object):
    def multiply(self, num1, num2):
        num_1 = list(num1)
        num_2 = list(num2)
        for i in range(len(num_1)):
            num_1[i] = int(num_1[i])
        for j in range(len(num_2)):
            num_2[j] = int(num_2[j])
        ans = []
        a_num_1 = num_1[::-1]
        a_num_2 = num_2[::-1]
        for i in range(len(a_num_1)):
            for j in range(len(a_num_2)):
                ans.append(a_num_1[i]*(10**i)*a_num_2[j]*(10**j))

        return str(sum(ans))

if __name__ == "__main__":
    num1 = "123"
    num2 = "456"
    solution = Solution()
    result = solution.multiply(num1,num2)
    print(result)