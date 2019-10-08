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

    def PrintListNode(self,head):
        p = head
        while p != None:
            print(p.val)
            p = p.next
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
    a1 = handle.CreatefromList(nums1,len(nums1))
    a2 = handle.CreatefromList(nums2,len(nums2))
    print("--------print ListNode1----------")
    handle.PrintListNode(a1)
    print("--------print ListNode2----------")
    handle.PrintListNode(a2)
    solution = Solution()
    a3 = solution.mergeTwoLists(a1,a2)
    print("--------print merged ListNode----------")
    handle.PrintListNode(a3)