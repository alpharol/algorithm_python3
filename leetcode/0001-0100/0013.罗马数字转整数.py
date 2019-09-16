#https://leetcode-cn.com/problems/roman-to-integer/

"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
输入: "III" 输出: 3
输入: "IV" 输出: 4
输入: "IX" 输出: 9
输入: "LVIII" 输出: 58 解释: L = 50, V= 5, III = 3.
输入: "MCMXCIV" 输出: 1994 解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""

###思路就是设置一个字典，然后从字符串里两个两个看，
# 如果这两个在字典里，说明是特殊规则，那么把这两个罗马字母代表的数字放到list里，然后去掉；
# 如果这两个字母不再的话，就说明罗马字母需要一个一个的看

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        num = []
        while s != "":
            if s[:2] in dict:
                num.append(dict[s[:2]])
                s = s[2:]
            else:
                num.append(dict[s[0]])
                s = s[1:]
        print(num)
        return sum(num)

if __name__ == "__main__":
    s = "LVIII"
    solution = Solution()
    result = solution.romanToInt(s)
    print(result)