#https://leetcode-cn.com/problems/repeated-string-match/

"""
给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。
举个例子，A = "abcd"，B = "cdabcdab"。
答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。
"""

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        list_A = list(A)
        tmp_1 = int(len(B)/len(A))
        tmp_2 = int(len(B)/len(A))+2
        for i in range(tmp_1,tmp_2+1):
            tmp_li = "".join(list_A*i)
            #print(tmp_li)
            if B in tmp_li:
                return i
        return -1

if __name__ == "__main__":
    A = "abcd"
    B = "cdabcdab"
    solution = Solution()
    result = solution.repeatedStringMatch(A,B)
    print(result)

