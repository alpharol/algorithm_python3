#https://leetcode-cn.com/problems/add-two-numbers/

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

#a = ListNode(0)
#print(a.next)

class Solution:
    def addTwoNumbers(self,l1:ListNode,l2:ListNode):
        node1 = l1
        result1 = ""
        while node1 is not None:
            result1 = str(node1.val) + result1
            node1= node1.next

        node2 = l2
        result2 = ""
        while node2 is not None:
            result2 = str(node2.val) + result2
            node2 = node2.next

        add = str(int(result1)+int(result2))

        l3 = l4 = ListNode(0)
        for index in range(len(add),0,-1):
            l3.next = ListNode(int(add[index-1]))
            l3 = l3.next
        return l4.next

