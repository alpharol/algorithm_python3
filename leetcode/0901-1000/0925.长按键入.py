#https://leetcode-cn.com/problems/long-pressed-name/

"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

示例 1：输入：name = "alex", typed = "aaleex";输出：true;解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：输入：name = "saeed", typed = "ssaaedd";输出：false;解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：输入：name = "leelee", typed = "lleeelee";输出：true
示例 4：输入：name = "laiden", typed = "laiden"'输出：true;解释：长按名字中的字符并不是必要的。
"""


#执行用时 :80 ms, 在所有 Python3 提交中击败了13.65%的用户
#内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.71%的用户
class Solution:
    def isLongPressedName(self, name: str, typed: str):
        name_list = [0]
        for i in range(len(name)):
            if len(name_list) == 0:
                name_list.append(name[i])
            else:
                if name[i] != str(name_list[-1])[0]:
                    name_list.append(name[i])
                else:
                    name_list[-1] = name_list[-1]+name[i]
        tmp_name = name_list[1:]
        #print(tmp_name)
        typed_list = [0]
        for i in range(len(typed)):
            if len(typed_list) == 0:
                typed_list.append(typed[i])
            else:
                if typed[i] != str(typed_list[-1])[0]:
                    #print(typed_list[-1][0])
                    typed_list.append(typed[i])
                else:
                    typed_list[-1] = typed_list[-1] + typed[i]
        tmp_typed = typed_list[1:]
        #print(tmp_typed)
        # print(tmp_typed[0])
        # print(len(tmp_typed[0]))
        # print(tmp_typed[0][0])
        if len(tmp_name) != len(tmp_typed):
            return False
        else:
            for i in range(len(tmp_typed)):
                if tmp_name[i][0] != tmp_typed[i][0] or len(tmp_name[i]) > len(tmp_typed[i]):
                    return False
            return True

if __name__ == "__main__":
    name = "hwjlqnyyyypmsfg"
    typed = "hwjllqnnyyyyyyypmsffgg"
    solution = Solution()
    result = solution.isLongPressedName(name,typed)
    print(result)

