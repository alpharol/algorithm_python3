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
    def CreatefromList(self, nums, n):
        if n <= 0:
            return False
        elif n == 1:
            return ListNode(nums[0])
        else:
            root = ListNode(nums[0])
            tmp = root
            for i in range(1, n):
                tmp.next = ListNode(nums[i])
                tmp = tmp.next
            return root

    def PrintListNode(self, head):
        p = head
        ans = []
        while p != None:
            ans.append(str(p.val))
            p = p.next
        print("->".join(ans))

###创建新结点的方法
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        h = head
        while h:
            if h.next:
                p.next = ListNode(h.next.val)
                p = p.next
                p.next = ListNode(h.val)
                p = p.next
                h = h.next.next
            else:
                p.next = h
                h = h.next
        return dummy.next
"""
####这个方法不需要创建新的结点，但是还没有弄明白
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         p = dummy
#         h = head
#         while h:
#             if h and h.next:
#                 tmp = h.next
#                 p.next = tmp
#                 tmp.next = h
#                 # 交换 位置
#                 #h.next = h.next.next
#                 h = h.next.next
#                 p = p.next.next
#             else:
#                 p.next = h
#                 h = h.next
#         return dummy.next

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    handle = ListNode_handle()
    a = handle.CreatefromList(nums, len(nums))
    handle.PrintListNode(a)
    # solution = Solution()
    # b = solution.swapPairs(a)
    # handle.PrintListNode(b)
