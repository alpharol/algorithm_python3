#https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

###从思路上来看：如果没有数字，返回一个空的列表
###如果又数字存在的话，由于数字的个数无法确认，所以只能一个一个来
class Solution:
    def letterCombinations(self, digits):
        dict = {'2':["a","b","c"],'3':["d","e","f"],'4':["g","h","i"],'5':["j","k","l"],
                '6':["m","n","o"],'7':["p","q","r","s"],'8':["t","u","v"],'9':["w","x","y","z"]}
        n = len(digits)
        if n == 0:
            return []
        else:
            i = 0
            re = [""]
            while i < n:
                mid = []
                for w in re:
                    for q in dict[digits[i]]:
                        tmp = w + q
                        mid.append(tmp)
                re = mid
                i = i + 1
            return re



if __name__ == "__main__":
    digits = "23"
    solution = Solution()
    result = solution.letterCombinations(digits)
    print(result)





