#https://leetcode-cn.com/problems/longest-palindrome/

"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:假设字符串的长度不会超过 1010。

示例 1:输入:"abccccdd";输出:7
解释:我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_li = list(s)
        dict = {}
        tmp = []
        for i in range(len(s_li)):
            if s_li[i] not in dict:
                dict[s_li[i]] = 1
            else:
                dict[s_li[i]] = dict[s_li[i]] + 1
        set_s = list(set(s_li))
        count = 0
        Flag = False
        for w in set_s:
            if dict[w] % 2 == 0:
                count = count + dict[w]
            else:
                Flag = True
                count = count + dict[w] - 1
        if Flag:
            return count + 1
        else:
            return count

if __name__ == "__main__":
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(result)
