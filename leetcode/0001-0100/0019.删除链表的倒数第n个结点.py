#https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明： n 保证是有效的。
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode_handle:
    def CreatefromList(self,nums,n):
        if n <= 0 :
            return False
        elif n == 1:
            return ListNode(nums[0])
        else:
            root=ListNode(nums[0])
            tmp = root
            for i in range(1,n):
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
###需要明白的是删除倒数第二个，相当于找到倒数第三个和倒数第一个


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        while n > 0:
            fast = fast.next
            n = n - 1
        slow = dummy
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next



if __name__ == "__main__":
    nums = [1,2,3,4,5]
    handle = ListNode_handle()
    a = handle.CreatefromList(nums,len(nums))
    handle.PrintListNode(a)
    solution = Solution()
    b = solution.removeNthFromEnd(a,2)
    handle.PrintListNode(b)

