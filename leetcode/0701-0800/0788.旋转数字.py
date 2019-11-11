#https://leetcode-cn.com/problems/rotated-digits/

"""
我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。
如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

示例:输入: 10;输出: 4
解释: 在[1, 10]中有四个好数： 2, 5, 6, 9。注意 1 和 10 不是好数, 因为他们在旋转之后不变。
"""

class Solution:
    def rotatedDigits(self, N: int):
        dict = {"0":"0","1":"1","2":"5","5":"2","6":"9","8":"8","9":"6"}
        count = 0
        for i in range(2,N+1):
            tmp = str(i)
            s = ""
            for j in range(len(tmp)):
                if tmp[j] not in dict.keys():
                    break
                else:
                    s = s + dict[tmp[j]]
            if len(s) == len(tmp) and int(s) != i:
                count = count + 1
        return count


if __name__ == "__main__":
    N = 15
    solution = Solution()
    result = solution.rotatedDigits(N)
    print(result)
