#https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""
#25ms+5728k
class Solution:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
    def push(self, node):
        a = self.stack_1
        a.append(node)
    def pop(self):
        while len(self.stack_1) > 1:
            self.stack_2.append(self.stack_1[-1])
            self.stack_1.pop(-1)
        res = self.stack_1[0]
        self.stack_1.pop(0)
        while self.stack_2 != []:
            self.stack_1.append(self.stack_2[-1])
            self.stack_2.pop(-1)
        return res

