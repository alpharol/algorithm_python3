# https://leetcode-cn.com/problems/swap-nodes-in-pairs/

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:给定 1->2->3->4, 你应该返回 2->1->4->3.
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

    def print_linked(self, root: ListNode):
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

    def length(self, root):
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

    def insert_link(self, root, num, position):
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

    def delete_link(self, root, position):
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



#*****************************************************#
#******************真正的题目在这里*********************#
#*****************************************************#
# 执行用时 :44 ms, 在所有 python3 提交中击败了70.57%的用户
# 内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.93%的用户
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        h = head
        while h != None:
            if h and h.next:
                tmp = h.next.next
                p.next = h.next
                p = p.next
                p.next = h
                p = p.next
                h = tmp
                p.next = h
            else:
                p.next = h
                h = h.next
        return dummy.next


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    handle = ListNode_handle()
    a = handle.Creatlist(nums)
    handle.print_linked(a)
    solution = Solution()
    b = solution.swapPairs(a)
    print("Done")
    handle.print_linked(b)
    print("Done")
