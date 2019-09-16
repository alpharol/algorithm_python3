# https://leetcode-cn.com/problems/plus-one/

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:输入: [1,2,3],输出: [1,2,4],解释: 输入数组表示数字 123。
示例 2:输入: [4,3,2,1],输出: [4,3,2,2],解释: 输入数组表示数字 4321。
"""


# ************************************#
# *************solution 2*************#
# ************************************#
#执行用时 :44 ms, 在所有 Python3 提交中击败了93.63%的用户
#内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.64%的用户
class Solution:
    def plusOne(self, digits):
        n = len(digits)-1
        while n >= 0:
            if digits[n] != 9:
                digits[n] = digits[n] + 1
                break
            else:
                digits[n] = 0
            n = n - 1
        if digits[0] == 0:
            digits.insert(0, 1)
            return digits
        else:
            return digits




if __name__ == "__main__":
    digits = [9]
    solution = Solution()
    result = solution.plusOne(digits)
    print(result)


    
# ************************************#
# *************solution 1*************#
# ************************************#
# 执行用时 :84 ms, 在所有 Python3 提交中击败了7.28%的用户
# 内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.64%的用户
###算法的时间复杂度是O(n)+O(n)
"""
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        ans = []
        s = str(int("".join(digits))+1)
        #print(s)
        for i in range(len(s)):
            ans.append(int(s[i]))
        return ans
"""
