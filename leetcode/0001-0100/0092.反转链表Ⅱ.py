# https://leetcode-cn.com/problems/reverse-linked-list-ii/

"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:1 ≤ m ≤ n ≤ 链表长度。
示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


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


# *****************************************************#
# ******************真正的题目在这里*********************#
# *****************************************************#
# 执行用时 :52 ms, 在所有 python3 提交中击败了32.72%的用户
# 内存消耗 :13.6 MB, 在所有 python3 提交中击败了5.24%的用户
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        i = 0
        stack = []
        while i < m - 1:
            p = p.next
            i = i + 1
        left = p
        while i >= m - 1 and i < n:
            stack.append(p.next)
            p = p.next
            i = i + 1
        right = p.next
        while stack != []:
            left.next = stack.pop()
            left = left.next
        left.next = right
        return dummy.next


if __name__ == "__main__":
    num = [1, 2, 3, 4, 5]
    handle = ListNode_handle()
    a = handle.Creatlist(num)
    handle.print_linked(a)
    solution = Solution()
    b = solution.reverseBetween(a, 2, 4)
    handle.print_linked(b)
