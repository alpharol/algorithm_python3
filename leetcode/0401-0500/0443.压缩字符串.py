#https://leetcode-cn.com/problems/string-compression/

"""
给定一组字符，使用原地算法将其压缩。
压缩后的长度必须始终小于或等于原数组长度。
数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
在完成原地修改输入数组后，返回数组的新长度。

 进阶：
你能否仅使用O(1) 空间解决问题？

示例 1：
输入：["a","a","b","b","c","c","c"]
输出：返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]
说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。

示例 2：
输入：["a"]
输出：返回1，输入数组的前1个字符应该是：["a"]
说明：
没有任何字符串被替代。
"""

class Solution:
    def compress(self, chars: list) -> int:
        count = 1
        for i in range(len(chars)-1,-1,-1):
            if i > 0 and chars[i] == chars[i-1]:
                count = count + 1
            else:
                end = i + count
                if count == 1:
                    chars[i:end] = [chars[i]]
                else:
                    chars[i:end] = [chars[i]] + list(str(count))
                    count = 1
        return chars

if __name__ == "__main__":
    chars = ["a","a","b","b","c","c","c"]
    solution = Solution()
    result = solution.compress(chars)
    print(result)
