#https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

"""
题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#25ms+5852k
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        p = listNode
        tmp = []
        while p != None:
            tmp.append(p.val)
            p = p.next
        return tmp[::-1]

