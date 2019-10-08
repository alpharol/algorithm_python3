# https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6?tpId=13&tqId=11163&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

###25ms+5860k
#斐波那契数列
class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            ans = [0, 1, 2]
            k = number - 2
            while k > 0:
                ans.append(ans[-1] + ans[-2])
                k = k - 1
            return ans[-1]
