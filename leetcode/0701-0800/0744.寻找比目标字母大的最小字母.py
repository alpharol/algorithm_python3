#https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/

"""
给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。
数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。

输入:letters = ["c", "f", "j"]target = "a";输出: "c"

输入:letters = ["c", "f", "j"]target = "c";输出: "f"

输入:letters = ["c", "f", "j"]target = "d";输出: "f"

输入:letters = ["c", "f", "j"]target = "g";输出: "j"

输入:letters = ["c", "f", "j"]target = "j";输出: "c"

输入:letters = ["c", "f", "j"]target = "k";输出: "c"
"""

class Solution:
    def nextGreatestLetter(self, letters: list, target: str) -> str:
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
        num = []
        for w in letters:
            num.append(alpha.index(w))
        #print(num)
        target_index = alpha.index(target)
        #print(target_index)
        for i in range(len(num)):
            if target_index < num[i]:
                return letters[i]
        return letters[0]

if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "k"
    solution = Solution()
    result = solution.nextGreatestLetter(letters,target)
    print(result)
