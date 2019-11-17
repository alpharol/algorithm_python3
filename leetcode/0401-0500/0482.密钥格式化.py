# https://leetcode-cn.com/problems/license-key-formatting/

"""
给定一个密钥字符串S，只包含字母，数字以及 '-'（破折号）。N 个 '-' 将字符串分成了 N+1 组。
给定一个数字 K，重新格式化字符串，除了第一个分组以外，每个分组要包含 K 个字符，第一个分组至少要包含 1 个字符。
两个分组之间用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。
给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。

示例 1：输入：S = "5F3Z-2e-9-w", K = 4;输出："5F3Z-2E9W"
解释：字符串 S 被分成了两个部分，每部分 4 个字符；
     注意，两个额外的破折号需要删掉。

示例 2：输入：S = "2-5g-3-J", K = 2;输出："2-5G-3J"
解释：字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。
"""


class Solution:
    def licenseKeyFormatting(self, S: str, K: int):
        li_s = "".join(S.split("-"))[::-1]
        print(li_s)
        res = []
        for i in range(len(li_s)):
            if (i + 1) % K != 0:
                res.append(li_s[i])
            else:
                res.append(li_s[i])
                res.append("-")
        if len(res) != 0 and res[-1] == "-": res.pop()
        return "".join(res[::-1]).upper()


if __name__ == "__main__":
    S = "---"
    K = 3
    solution = Solution()
    result = solution.licenseKeyFormatting(S, K)
    print(result)
