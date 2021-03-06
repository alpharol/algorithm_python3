#https://leetcode-cn.com/problems/merge-two-sorted-lists/

"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
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



#执行用时 :56 ms, 在所有 Python3 提交中击败了77.70%的用户
#内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.66%的用户

#************************************************************#
#**********************真正的题目在这里*************************#
#************************************************************#
class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        dummy = ListNode(0)
        tmp = dummy
        p1 = l1
        p2 = l2
        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                tmp.next = p1
                tmp = p1
                p1 = p1.next
            else:
                tmp.next = p2
                tmp = p2
                p2 = p2.next
        if p1 == None:
            while p2 != None:
                tmp.next = p2
                tmp = tmp.next
                p2 = p2.next
        else:
            while p1 != None:
                tmp.next = p1
                tmp = tmp.next
                p1 = p1.next
        return dummy.next



if __name__ == "__main__":
    nums1 = [1,3,5,7,9,14,19,20]
    nums2 = [2,4,6,8,10,11]
    handle = ListNode_handle()
    a1 = handle.Creatlist(nums1)
    a2 = handle.Creatlist(nums2)
    print("--------print ListNode1----------")
    handle.print_linked(a1)
    print("--------print ListNode2----------")
    handle.print_linked(a2)
    solution = Solution()
    a3 = solution.mergeTwoLists(a1,a2)
    print("--------print merged ListNode----------")
    handle.print_linked(a3)