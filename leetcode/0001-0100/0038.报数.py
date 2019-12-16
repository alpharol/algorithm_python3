#https://leetcode-cn.com/problems/count-and-say/

"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
"""
# 执行用时 :32 ms, 在所有 python3 提交中击败了99.47%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.45%的用户
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        elif n == 3:
            return "21"
        elif n == 4:
            return "1211"
        else:
            x = 4
            s = "1211"
            while x < n:
                tmp = s[0]
                flag = 1
                li = []
                for i in range(1,len(s)):
                    if tmp == s[i]:
                        flag = flag + 1
                    else:
                        li.append(str(flag))
                        li.append(str(tmp))
                        tmp = s[i]
                        flag = 1
                li.append(str(flag))
                li.append(str(tmp))
                s = "".join(li)
                x = x + 1
            return s


if __name__ == "__main__":
    n =7
    solution = Solution()
    result = solution.countAndSay(n)
    print(result)



