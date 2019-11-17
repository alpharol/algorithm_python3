#https://leetcode-cn.com/problems/happy-number/

"""
编写一个算法来判断一个数是不是“快乐数”。
一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，
也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 输入: 19;输出: true
"""

class Solution(object):
    def isHappy(self, n):
        previous = set()
        while n != 1:
            num = 0
            while n > 0:
                tmp = n%10
                num = num + tmp**2
                n = n // 10

            if num in previous:
                return False
            else:
			    pass

            previous.add(num)
            n = num
        return True

if __name__ == "__main__":
    n = 19
    solution =Solution()
    result = solution.isHappy(n)
    print(result)