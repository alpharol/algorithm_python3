#https://leetcode-cn.com/problems/buddy-strings/

"""
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，
就返回 true ；否则返回 false 。

示例 1：输入： A = "ab", B = "ba";输出： true
示例 2：输入： A = "ab", B = "ab";输出： false
示例 3:输入： A = "aa", B = "aa";输出： true
示例 4：输入： A = "aaaaaaabc", B = "aaaaaaacb";输出： true
示例 5：输入： A = "", B = "aa";输出： false
"""

class Solution:
    def buddyStrings(self, A: str, B: str):
        a = []
        b = []
        if len(A) != len(B):
            return False
        else:
            for i in range(len(A)):
                if A[i] != B[i]:
                    a.append(A[i])
                    b.append(B[i])
            if len(a) != 2 and len(a) != 0:
                return False
            elif len(a) == 0:
                #print(len(set(A)))
                if len(A) - len(set(A)) >= 1:
                    return True
                else:
                    return False
            else:
                if a[::-1] != b:
                    return False
        return True

if __name__ == "__main__":
    A = ""
    B = "aa"
    solution = Solution()
    result = solution.buddyStrings(A,B)
    print(result)


