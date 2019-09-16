#https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
#27ms+6660k
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        li = s.split(" ")
        return "%20".join(li)

if __name__ == "__main__":
    s = "Hello World"
    solution = Solution()
    result = solution.replaceSpace(s)
    print(result)