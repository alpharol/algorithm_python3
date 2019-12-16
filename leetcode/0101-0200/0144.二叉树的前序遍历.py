#https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

"""
给定一个二叉树，返回它的 前序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,2,3]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        if root == None:
            return []
        else:
            result = [root.val]
            left = self.preorderTraversal(root.left)
            right = self.preorderTraversal(root.right)
        return result + left + right