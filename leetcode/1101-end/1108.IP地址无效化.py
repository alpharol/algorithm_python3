#https://leetcode-cn.com/problems/defanging-an-ip-address/

"""
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。

示例 1：输入：address = "1.1.1.1";输出："1[.]1[.]1[.]1"
示例 2：输入：address = "255.100.50.0";输出："255[.]100[.]50[.]0"
 
提示：给出的 address 是一个有效的 IPv4 地址
"""

#执行用时 :52 ms, 在所有 Python3 提交中击败了41.88%的用户
#内存消耗 :14 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def defangIPaddr(self, address: str) -> str:
        tmp = address.replace(".","[.]")
        return tmp

if __name__ == "__main__":
    address = "255.100.50.0"
    solution = Solution()
    result = solution.defangIPaddr(address)
    print(result)