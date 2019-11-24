# https://leetcode-cn.com/problems/add-two-numbers/

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


class ListNode_handle:
    def Creatlist(self, li):
        """
        从列表创建一个链表
        :param li: 列表
        :return: 头结点
        """
        if len(li) <= 0:
            return False
        if len(li) == 1:
            return ListNode(li[0])  # 只有一个节点
        else:
            root = ListNode(li[0])
            tmp = root
            for i in range(1, len(li)):
                tmp.next = ListNode(li[i])
                tmp = tmp.next
            return root

    def print_linked(self,root: ListNode):
        """
        打印链表
        :param root: 头结点
        :return: 打印链表
        """
        value = []
        tmp = root
        while tmp.next != None:
            value.append(str(tmp.val))
            tmp = tmp.next
        value.append(str(tmp.val))
        print("->".join(value))

    def length(self,root):
        """
        计算链表的长度
        :param root:
        :return:
        """

        tmp = root
        root_length = 0
        while tmp.next != None:
            root_length = root_length + 1
            tmp = tmp.next
        root_length = root_length + 1
        return root_length

    def insert_link(self,root, num, position):
        """
        向链表插入数据
        :param root: 头结点
        :param num: 插入的数据
        :return: 头结点
        """
        root_length = ListNode_handle.length(root)
        if position <= 0 or position > root_length + 2:
            print("the position is not right")
            return root
        elif position == 1:
            tmp = ListNode(num)
            tmp.next = root
            return tmp
        else:
            tmp = ListNode(0)
            tmp.next = root
            i = 1
            while i < position:
                tmp = tmp.next
                i = i + 1
            insert_node = ListNode(num)
            insert_node.next = tmp.next
            tmp.next = insert_node
        return root

    def delete_link(self,root, position):
        """
        删除链表中的元素
        :param root: 头结点
        :param position: 删除的位置
        :return: 返回新链表的头结点
        """
        if position < 1 or position > ListNode_handle.length(root):
            print("the position is not right")
            return root
        elif position == 1:
            return root.next
        else:
            tmp = ListNode(0)
            tmp.next = root
            i = 1
            while i < position:
                tmp = tmp.next
                i = i + 1
            tmp.next = tmp.next.next
            return root


# 执行用时 :76 ms, 在所有 python3 提交中击败了93.20%的用户
# 内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.06%的用户
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        node1 = l1
        result1 = ""
        while node1 is not None:
            result1 = str(node1.val) + result1
            node1 = node1.next

        node2 = l2
        result2 = ""
        while node2 is not None:
            result2 = str(node2.val) + result2
            node2 = node2.next

        add = str(int(result1) + int(result2))

        l3 = l4 = ListNode(0)
        for index in range(len(add), 0, -1):
            l3.next = ListNode(int(add[index - 1]))
            l3 = l3.next
        return l4.next


if __name__ == "__main__":
    nums1 = [2, 4, 3]
    nums2 = [5, 6, 4]
    handle = ListNode_handle()
    root1 = handle.Creatlist(nums1)
    root2 = handle.Creatlist(nums2)
    handle.print_linked(root1)
    handle.print_linked(root2)
    solution = Solution()
    result = solution.addTwoNumbers(root1, root2)
    handle.print_linked(result)
